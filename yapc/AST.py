import pydot
from ErrorHandler import *
from SymbolTable import *


def traverse_skew_tree(node, stop_node_type=None):
    """
    遍历一种很特殊但是在我们的 parse tree 中频繁出现的一种结构（左递归导致的）
    能不能顺便做一个 compress ✅
    :param node:
    :return: flattened subtree
    """
    descending_leaves = []
    children = node.children
    for child in children:
        if isinstance(child, Node):
            if child.type == stop_node_type:
                descending_leaves.append(child)
            else:
                descending_leaves.extend(traverse_skew_tree(child, stop_node_type))
        else:
            # reach the leaf node
            descending_leaves.append(child)

    return tuple(descending_leaves)


class Node(object):

    def __init__(self, t, *args):
        self._type = t
        self._children = args

    @property
    def children(self):
        return self._children

    @property
    def type(self):
        return self._type

    # TODO: this __str__ is not clear
    def __str__(self):
        # s = "Node type: %s" % self._type/
        s = "type: " + str(self._type) + "\n"
        # s += "".join(["i: " + str(i) + "\n" for i in self._children])
        return s


def parse_range_from_range_node(Node):
    # parse tree error
    assert Node.type == 'range', Node.type
    assert len(Node.children) == 2, Node.children

    left_range_node, right_range_node = Node.children
    left_type, right_type = left_range_node.type, right_range_node.type
    # semantic error
    if left_type != right_type:
        raise Exception('left range type: `{}`, right range type: `{}`'.format(left_type, right_type))

    if left_type not in ['integer', 'char']:
        raise Exception('arr only supprt integer / char indices, not {}'.format(left_type))

    left_val, *_ = left_range_node.children
    right_val, *_ = right_range_node.children

    if left_val > right_val:
        raise Exception('left range val `{}` > right range val `{}`'.format(left_val, right_val))
    return left_type, left_val, right_val


def parse_type_definition_from_type_node(node):
    """
    parse type_definition node, return symb tab item
    :param node:
    :return:
    """
    assert node.type == 'type_definition', node.type
    children = node.children
    assert len(children) == 2, children
    id_, type_node = children
    assert type_node.type in ['alias', 'sys_type', 'array']
    if type_node.type == 'alias':
        # most simple
        type_alias, *_ = type_node.children
        return 'alias', id_, type_alias
    elif type_node.type == 'sys_type':
        sys_type, *_ = type_node.children
        return 'sys_type', id_, sys_type
    else:
        # 1d array, compicated
        index_type, element_type, left_val, right_val = parse_array_from_array_node(type_node)
        return 'array', id_, index_type, element_type, left_val, right_val


def parse_array_from_array_node(arr_node):
    assert arr_node.type == 'array', arr_node.type
    range_node, sys_type_node = arr_node.children
    index_type, left_val, right_val = parse_range_from_range_node(range_node)
    element_type = sys_type_node.children[0]
    return index_type, element_type, left_val, right_val


def parse_var_decl_from_node(var_decl_node):
    """
    parse var decl node,
    :param var_decl_node:
    :return: flatten name list and associated symb_tab_item
    """
    assert var_decl_node.type == 'var_decl', var_decl_node.type
    maybe_name_list_node, type_decl_node = var_decl_node.children

    # get name_list
    if isinstance(maybe_name_list_node, Node):
        # traverse name_list
        flatten_name_list = traverse_skew_tree(maybe_name_list_node)
        # flatten the subtree for future use
        maybe_name_list_node._children = flatten_name_list
    else:
        # just a leaf node
        flatten_name_list = [maybe_name_list_node]

    # get the var type
    assert type_decl_node.type in ['sys_type', 'array'], type_decl_node.type
    if type_decl_node.type == 'sys_type':
        var_type, *_ = type_decl_node.children
        symb_tab_item = SymbolTableItem('var', {'var_type': var_type})
    elif type_decl_node.type == 'array':
        index_type, element_type, left_val, right_val = parse_array_from_array_node(type_decl_node)
        symb_tab_item = SymbolTableItem('arr_var',
                                        {'index_type': index_type,
                                         'index_range': (left_val, right_val),
                                         'element_type': element_type})
    return flatten_name_list, symb_tab_item


def graph(node, filename):
    edges = descend(node)
    g = pydot.graph_from_edges(edges)
    if filename:
        f = filename + ".png"
    else:
        f = "graph.png"
    g.write_png(f, prog='dot')


def descend(node):
    edges = []
    if node.__class__ != Node:
        return []

    for i in node.children:
        edges.append((s(node), s(i)))
        edges += descend(i)
    return edges


def s(node):
    if node.__class__ != Node:
        return "%s (%s)" % (node, id(node))
    return "%s (%s)" % (node.type, id(node))
