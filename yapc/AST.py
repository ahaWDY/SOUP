import pydot
from ErrorHandler import *
from SymbolTable import *
import copy
from functools import reduce
from utils import *
import random


def traverse_skew_tree(node, stop_node_type=None):
    # TODO: find bug
    """
    遍历一种很特殊但是在我们的 parse tree 中频繁出现的一种结构（左递归导致的）
    能不能顺便做一个 compress ✅
    :param stop_node_type:
    :param node:
    :return: flattened subtree
    """
    if not isinstance(stop_node_type, list):
        stop_node_type = [stop_node_type]
    descending_leaves = []
    children = node.children
    for child in children:
        if isinstance(child, Node):
            if child.type in stop_node_type:
                descending_leaves.append(child)
            else:
                descending_leaves.extend(traverse_skew_tree(child, stop_node_type))
        elif child is None:
            pass
        else:
            # reach the leaf node
            descending_leaves.append(child)

    return tuple(descending_leaves)


def traverse_skew_tree_bool(node, stop_node_type, target_node_type):
    descending_leaves = []
    children = node.children
    if node.type != target_node_type:
        descending_leaves.append(node)
        return tuple(descending_leaves)
    for child in children:
        if isinstance(child, Node):
            if child.type.startswith(stop_node_type):
                descending_leaves.append(child)
            else:
                descending_leaves.extend(traverse_skew_tree_bool(child, stop_node_type, target_node_type))
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


def parse_type_definition_from_type_node(node, symbol_table):
    """
    parse type_definition node, only return information
    :param symbol_table:
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
        # 1d array, complicated
        index_type, element_type, left_val, right_val = parse_array_from_array_node(type_node, symbol_table)
        return 'array', id_, index_type, element_type, left_val, right_val


def parse_type_decl_node(type_decl_node, symbol_table):
    """
    grammar rule:
        * type_decl         : simple_type_decl
                            | array_type_decl
        * simple_type_decl  :  SYS_TYPE
                            |  LP  name_list  RP (enum)
                            |  const_value  DOTDOT  const_value (range)
                            |  ID
        * array_type_decl   :  kARRAY  LB  simple_type_decl  RB  kOF  type_decl
    :param symbol_table:
    :param type_decl_node:
    :return: type(sys_type from [integer, real, char]) / array_type(Array Type instance)
    """
    if type_decl_node.type == 'sys_type':
        sys_type = type_decl_node.children[0]
        return sys_type
    elif type_decl_node.type == 'alias':
        # check whether the alias type exits
        alias_type = type_decl_node.children[0]
        ret_val = symbol_table.chain_look_up(alias_type)
        if not ret_val:
            raise Exception('alias type: `{}` used before defined'.format(alias_type))
        # return the true type
        if ret_val.type == 'sys_type':
            return ret_val.value['sys_type']
        else:  # array type
            return ret_val.value

    elif type_decl_node.type == 'array':
        index_type, element_type, left_val, right_val = parse_array_from_array_node(type_decl_node, symbol_table)
        return ArrayType(index_type, (left_val, right_val), element_type)

    else:
        raise NotImplementedError('{}'.format(type_decl_node.type))


def parse_array_from_array_node(arr_node, symbol_table):
    """
    :param arr_node:
    :param symbol_table:
    :return: symb_tab_item to be inserted
    """
    assert arr_node.type == 'array', arr_node.type
    range_node, type_node = arr_node.children
    index_type, left_val, right_val = parse_range_from_range_node(range_node)
    element_type = parse_type_decl_node(type_node, symbol_table)
    return index_type, element_type, left_val, right_val


def parse_var_decl_from_node(var_decl_node, symbol_table):
    """
    parse var decl node,
    :param var_decl_node:
    :param symbol_table:
    :return: flatten name list and associated symb_tab_item
    """
    assert var_decl_node.type == 'var_decl', var_decl_node.type
    maybe_name_list_node, type_decl_node = var_decl_node.children

    flatten_name_list = parse_name_list(maybe_name_list_node)

    # get the var type
    assert type_decl_node.type in ['sys_type', 'array', 'alias'], type_decl_node.type
    if type_decl_node.type == 'sys_type':
        var_type, *_ = type_decl_node.children
        symb_tab_item = SymbolTableItem('var', {'var_type': var_type})
    elif type_decl_node.type == 'array':
        index_type, element_type, left_val, right_val = parse_array_from_array_node(type_decl_node, symbol_table)
        array_type = ArrayType(index_type, (left_val, right_val), element_type)
        symb_tab_item = SymbolTableItem('arr_var',
                                        array_type)
    else:  # alias
        alias_type = type_decl_node.children[0]
        ret_val = symbol_table.chain_look_up(alias_type)
        if not ret_val:
            raise Exception('alias type {} used before defined'.format(alias_type))
        else:
            symb_tab_item = ret_val

    return flatten_name_list, symb_tab_item


def constant_folding(node, symbol_table):
    """
    一个整体逻辑是这样的
    如果返回值为 None, 证明这个节点不能完全的 const fold
    如果返回值不为 None, 那么这个节点可以完全的 const fold, caller 只需要让孩子变成这个值即可
    但是这个函数缺陷很大坑也很大，有机会要重新写一遍
    """
    return None

    # if not isinstance(node, Node):  # id (一般是 constant 的名字或者 function 的名字 / variable)
    #     id_ = node
    #     # 去 symbol table 查找, 这里需要 chain_lookup, 右值可存在于之前的 scope
    #     ret_val = symbol_table.chain_look_up(id_)
    #     if not ret_val:
    #         raise Exception('`{}` is not a function or a constant or variable'.format(id_))
    #     assert ret_val.type in ['const', 'var'], ret_val.type
    #     if ret_val.type == 'const':
    #         return ret_val.value['const_val']
    #     else:
    #         return None
    #
    # elif node.type == 'expression':  # bool const
    #     if len(node.children) == 1:
    #         val = constant_folding(node.children[0], symbol_table)
    #         # if val is not None:
    #         #     node._children = [val]
    #         return val
    #     else:
    #         left_val = constant_folding(node.children[0], symbol_table)
    #         right_val = constant_folding(node.children[2], symbol_table)
    #         if left_val is not None and right_val is not None:
    #             return bool_op_to_func[node.children[1]](left_val, right_val)
    #         else:
    #             return None
    #
    # elif node.type in ['integer', 'real', 'char', 'sys_con']:  # 直接的常数 1, 1.3, c, true
    #
    #     val = node.children[0]
    #     if node.type == 'sys_con':
    #         return bool_dict[val]
    #     else:
    #         return val
    # elif node.type == 'factor-arr':
    #
    #     arr_id, right_child = node.children
    #     # 需要进行 chain look up
    #     arr_id_lookup = symbol_table.chain_look_up(arr_id)
    #     if arr_id_lookup is None:
    #         raise Exception('{} used before declaration'.format(arr_id))
    #     right_val = constant_folding(right_child, symbol_table)
    #     if right_val is not None:
    #         node._children = (arr_id, right_val)
    #     return None  # return None, because the factor-arr is known to be non-const
    # elif node.type == 'factor-func':
    #     pass
    # elif node.type == 'factor':
    #     # kNOT factor
    #     # SUBSTRACT factor
    #     unary_op, right_child = node.children
    #     if unary_op == 'not':  # not true
    #         second_val = constant_folding(right_child, symbol_table)
    #         if second_val is not None:
    #             node._children = (unary_op, second_val)
    #             return not second_val
    #         else:
    #             return None
    #     elif unary_op == '-':
    #         second_val = constant_folding(right_child, symbol_table)
    #         if second_val is not None:
    #             node._children = (unary_op, second_val)
    #             return -second_val
    #         else:
    #             return None
    #     else:
    #         raise Exception('factor node with unknown unary op: {}'.format(unary_op))
    #
    # else:  # internal node, term  / expr
    #     node_type = node.type
    #
    #     arithmic_func = bin_op_to_func[type_to_bin_op[node_type]]
    #     children = node.children
    #     val_list = []
    #     can_const_fold = True
    #     new_children = []
    #
    #     for idx, child in enumerate(children):
    #         val = constant_folding(child, symbol_table)
    #         if val is None:
    #             can_const_fold = False
    #             new_children.append(child)
    #         else:
    #             val_list.append(val)
    #             new_children.append(val)
    #     node._children = tuple(new_children)
    #     if can_const_fold:
    #         return reduce(arithmic_func, val_list)
    #     else:
    #         return None


def parse_para_decl_list(ast_node, symb_tab_node):
    """
    需要建一个新的 symbol table
    :param node: ast node
    :param symbol_table_node: symb_tab node
    :return:
    """
    if ast_node.type == 'para_decl_list':
        # flatten
        ast_node._children = traverse_skew_tree(ast_node, ['val_para_type_list', 'var_para_type_list'])
        var_val_declare_list = []
        for child in ast_node.children:
            var_val_declare_list.append(parse_var_val_para_type_list(child, symb_tab_node))
        return var_val_declare_list
    else:  # 只有一个 para_decl 的情况
        return [parse_var_val_para_type_list(ast_node, symb_tab_node)]


def parse_var_val_para_type_list(ast_node, symb_tab_node):
    """
    需要在 symbtab 中插入这些 para declaration
    parse var_para_type_list|val_para_type_list
    :param ast_node:
    :param symb_tab_node:
    :return:
    """
    left_child, right_child = ast_node.children
    name_list = parse_name_list(left_child)
    type_ = parse_type_decl_node(right_child, symb_tab_node)
    for name in name_list:
        # TODO: 暂时把所有参数在新的 scope 下存成 var 型
        if symb_tab_node.lookup(name):
            raise Exception("parameter `{}` is already defined".format(name))
        symb_tab_item = SymbolTableItem('var', {'var_type': type_})
        symb_tab_node.insert(name, symb_tab_item)
    if ast_node.type == 'var_para_type_list':  # var_para_type_list

        return 'var', name_list, type_
    else:  # val_para_type_list
        return 'val', name_list, type_


# TODO: traverse_skew version
def parse_name_list(ast_node):
    """
    maybe name_list or just a str
    """
    if isinstance(ast_node, str):
        # if symb_tab_node.lookup(ast_node) is not None:
        #     raise Exception('variable {} is already defined'.format(ast_node))
        return [ast_node]

    elif ast_node.type == 'name_list':
        left_child, right_child = ast_node.children
        name_list = parse_name_list(left_child) + parse_name_list(right_child)
        return name_list

    else:
        raise NotImplementedError("{} is not supported when parsing name_list node".format(ast_node.type))


def parse_procedure_decl_node(ast_node, symb_tab_node):
    """
    parse procedure declaration
    """
    proc_head_node, routine_node = ast_node.children
    proc_id, para_decl_list_node = proc_head_node.children
    ret_val = symb_tab_node.lookup(proc_id)
    if ret_val is not None:  # 是否定义
        raise Exception('procedure `{}` is already defined'.format(proc_id))

    # parse para_decl_list

    new_symb_tab_node = SymbolTableNode(proc_id, None, None)
    make_parent_and_child(symb_tab_node, new_symb_tab_node)

    if para_decl_list_node:
        var_val_para_type_list = parse_para_decl_list(para_decl_list_node, new_symb_tab_node)
    else:
        var_val_para_type_list = []
    # parse routine_node

    parse_routine_node(routine_node, new_symb_tab_node)

    return proc_id, var_val_para_type_list


def parse_routine_head_node(ast_node, symb_tab_node):
    """
    routine_head : const_part type_part var_part routine_part
    routine_head 保证有四个孩子
    """
    const_part_node, type_part_node, var_part_node, routine_part_node = ast_node.children
    if const_part_node:
        parse_const_node(const_part_node, symb_tab_node)
    if type_part_node:
        parse_type_part_node(type_part_node, symb_tab_node)
    if var_part_node:
        parse_var_part_node(var_part_node, symb_tab_node)
    if routine_part_node:
        parse_routine_part_node(routine_part_node, symb_tab_node)


def parse_const_node(ast_node, symb_tab_node):
    """
    const declaration
    const_expr_list or const_expr
    """

    const_expr_node_list = []
    if ast_node.type == 'const_expr':
        const_expr_node_list.append(ast_node)
    else:
        # flatten the sub tree
        ast_node._children = traverse_skew_tree(ast_node, 'const_expr')
        const_expr_node_list.extend(ast_node.children)

    for child in const_expr_node_list:
        id_, const_val_node = child.children
        const_type = const_val_node.type
        const_val, *_ = const_val_node.children
        const_val = CONST_TYPE_TO_FUNC[const_type](const_val)
        symb_tab_item = SymbolTableItem('const', {'const_val': const_val, 'const_type': const_type})
        is_conflict, ret_val = symb_tab_node.insert(id_, symb_tab_item)
        if is_conflict:
            raise ConflictIDError(id_, ret_val)


def parse_type_part_node(ast_node, symb_tab_node):
    """
    type part declaration
    type_decl_list or type_definition
    """
    if ast_node.type == 'type_definition':
        type_definition_node_list = [ast_node]
    else:  # type_decl_list

        # flatten type definitions
        ast_node._children = traverse_skew_tree(ast_node, 'type_definition')
        type_definition_node_list = ast_node.children

    for child in type_definition_node_list:
        # parse type_definition
        type_, id_, *attributes = parse_type_definition_from_type_node(child, symb_tab_node)

        if type_ == 'alias':
            # check whether the alias type exist
            type_alias = attributes[0]
            ret_val = symb_tab_node.lookup(type_alias)
            if not ret_val:
                raise Exception('type alias: `{}` used before defined'.format(type_alias))
            symb_tab_item = copy.deepcopy(ret_val)

        elif type_ == 'sys_type':
            sys_type = attributes[0]
            symb_tab_item = SymbolTableItem('sys_type', {'sys_type': sys_type})

        elif type_ == 'array':  # array type
            index_type, element_type, left_val, right_val = attributes
            array_type = ArrayType(index_type, (left_val, right_val), element_type)
            symb_tab_item = SymbolTableItem('arr_var',
                                            array_type)
        else:  # TODO: add record support
            raise NotImplementedError

        # insert into symbol table
        is_conflict, ret_val = symb_tab_node.insert(id_, symb_tab_item)

        if is_conflict:
            raise ConflictIDError(id_, symb_tab_item)


def parse_var_part_node(ast_node, symb_tab_node):
    """
    var part declaration
    var_decl_list or var_decl
    """

    if ast_node.type == 'var_decl':
        flatten_name_list, symb_tab_item = parse_var_decl_from_node(ast_node, symb_tab_node)
        # insert (name, type) in symbol table
        for id_ in flatten_name_list:
            is_conflict, ret_val = symb_tab_node.insert(id_, symb_tab_item)
            if is_conflict:
                raise ConflictIDError(id_, symb_tab_item)
    else:
        # flatten var_decl

        ast_node._children = traverse_skew_tree(ast_node, 'var_decl')

        for child in ast_node.children:
            flatten_name_list, symb_tab_item = parse_var_decl_from_node(child, symb_tab_node)

            # insert (name, type) in symbol table
            for id_ in flatten_name_list:
                is_conflict, ret_val = symb_tab_node.insert(id_, symb_tab_item)
                if is_conflict:
                    raise ConflictIDError(id_, symb_tab_item)


def parse_routine_part_node(ast_node, symb_tab_node):
    """
    parse routine part node
    return all (proc_id, var_val_para_type_list)
    一个 routine_part 里的 procedure 范围是同级的
    """
    proc_info_list = []
    # 如果只有一个 procedure, rountine_part 直接为一个 procedure_decl
    if ast_node.type == 'procedure_decl':
        proc_id, var_val_para_type_list = parse_procedure_decl_node(ast_node, symb_tab_node)
        proc_info_list.append((proc_id, var_val_para_type_list))
    elif ast_node.type == 'routine_part':
        flatten_proc_decl_nodes = traverse_skew_tree(ast_node, 'procedure_decl')
        ast_node._children = flatten_proc_decl_nodes
        proc_info_list = []
        for child in ast_node.children:
            proc_id, var_val_para_type_list = parse_procedure_decl_node(child, symb_tab_node)
            proc_info_list.append((proc_id, var_val_para_type_list))

    else:
        raise NotImplementedError

    for proc_id, var_val_para_type_list in proc_info_list:
        symb_tab_item = ProcedureItem(var_val_para_type_list, [])
        symb_tab_node.insert(proc_id, symb_tab_item)


def parse_routine_node(ast_node, symb_tab_node):
    """
    routine : routine_head routine_body
    routine_body: compound_stmt : stmt_list
    routine_head 节点一定会存在
    routine_body 可能不存在
    """
    routine_head_node, routine_body_node = ast_node.children
    if routine_head_node:
        parse_routine_head_node(routine_head_node, symb_tab_node)
    if routine_body_node:
        parse_stmt_list_node(routine_body_node, symb_tab_node)


def parse_stmt_list_node(ast_node, symb_tab_node):
    """
    stmt_list : stmt_list stmt SEMICON | empty
    确保一定不为 None
    哪怕只有一个 stmt, 还是会有 stmt_list 作为一个父节点
    """
    flatten_stmt_node_list = traverse_skew_tree(ast_node, [
        'assign_stmt', 'assign_stmt-arr', 'assign_stmt-record',
        'proc_stmt', 'proc_stmt-simple',
        'if_stmt', 'repeat_stmt', 'while_stmt', 'for_stmt'
    ])
    ast_node._children = flatten_stmt_node_list
    for child in ast_node.children:
        parse_stmt_node(child, symb_tab_node)


def parse_stmt_node(ast_node, symb_tab_node):
    """
    parse stmt node
    stmt :  INTEGER  COLON  non_label_stmt 这一情况的 node 叫 stmt-label
         |  non_label_stmt 这种情况的 node 直接叫 assgin 等
    """
    if ast_node.type == 'stmt-label':
        # TODO: add support for labeled statement
        raise NotImplementedError
    else:
        '''non_label_stmt :  assign_stmt 
                          | proc_stmt 
                          | compound_stmt 
                          | if_stmt 
                          | repeat_stmt 
                          | while_stmt 
                          | for_stmt 
                          | case_stmt 
                          | goto_stmt'''
        if ast_node.type.startswith('assign_stmt'):
            parse_assign_stmt_node(ast_node, symb_tab_node)
        elif ast_node.type.startswith('proc_stmt'):
            parse_proc_stmt_node(ast_node, symb_tab_node)
        else:
            raise NotImplementedError(ast_node.type)


def parse_proc_stmt_node(ast_node, symb_tab_node):
    """
    pass proc_stmt
    proc_stmt :  ID             // proc_stmt-simple node
              |  SYS_PROC       // proc_stmt-simple node
              |  ID  LP  args_list  RP  // proc_stmt node
              |  SYS_PROC  LP  expression_list  RP
              |  kREAD  LP  factor  RP
    """
    if ast_node.type == 'proc_stmt-simple':
        proc_id_or_sys_func, = ast_node.children
        if proc_id_or_sys_func in SYS_PROC:  # sys func
            pass
        else:
            # 检查该 procedure 是否定义过，chain look up
            ret_val = symb_tab_node.chain_look_up(proc_id_or_sys_func)
            if ret_val is None:
                raise Exception("procedure `{}` used before defined".format(proc_id_or_sys_func))
            # 并且该 procedure 不接受任何参数，事实上 parse 直接替我们做了这件事情，所以不需要额外检查
    else:  # proc_stmt node
        proc_id, right_child = ast_node.children
        if proc_id == 'read':
            parse_expression_node(ast_node, symb_tab_node)
        elif proc_id in SYS_PROC:  # write/writeln
            parse_expression_list(right_child, symb_tab_node)
        else:  # user defind proc
            # proc_stmt: ID  LP  args_list  RP
            # 检查 proc_id 是否定义过, chain_look_up
            ret_val = symb_tab_node.chain_look_up(proc_id)
            if ret_val is None:
                raise Exception("procedure `{}` used before declared".format(proc_id))
            else:
                # 检查变量个数是否合适
                # 用的变量是否定义过, 在 parse_args_list 中会自然调用 constant_folding, 会自动检查
                # TODO 用的变量类型是否合适
                param_list = ret_val.para_list
                n_args = parse_args_list(right_child, symb_tab_node)
                if len(param_list) != n_args:
                    raise Exception("procedure `{}` expect {} args, got {}".format(proc_id, len(param_list), n_args))


def parse_args_list(ast_node, symb_tab_node):
    """
    args_list :  args_list  COMMA  expression
              |  expression
    :return number of args
    """
    if len(ast_node.children) == 2:
        # traverse skew tree
        ast_node._children = traverse_skew_tree(ast_node, 'expression')
        new_children = []
        for child in ast_node.children:
            # fold constant
            val = constant_folding(child, symb_tab_node)
            if val is not None:
                new_children.append(val)
            else:
                new_children.append(child)
        ast_node._children = tuple(new_children)
        return len(ast_node.children)

    else:
        constant_folding(ast_node.children[0], symb_tab_node)
        return 1


def parse_assign_stmt_node(ast_node, symb_tab_node):

    """
    type checking and constant folding
    """

    children = ast_node.children
    if ast_node.type == 'assign_stmt':  # ID ASSIGN expression
        id_, expression_node = children
        ret_val = symb_tab_node.lookup(id_)
        if ret_val is None:
            raise Exception('var {} assigned before declared'.format(id_))
        if ret_val.type == 'const':
            raise Exception('const {} cannot be assigned!'.format(id_))

        constant_fold_ret = constant_folding(expression_node, symb_tab_node)
        if constant_fold_ret is not None:
            ast_node._children = (id_, constant_fold_ret)

    elif ast_node.type == 'assign_stmt-arr':  # ID LB expression RB ASSIGN expression
        id_, index_expression_node, expression_node = children
        ret_val = symb_tab_node.lookup(id_)
        if ret_val is None:
            raise Exception('var {} assigned before declared'.format(id_))
        if ret_val.type == 'const':
            raise Exception('const {} cannot be assigned!'.format(id_))
        constant_fold_ret = constant_folding(expression_node, symb_tab_node)
        index_fold_ret = constant_folding(index_expression_node, symb_tab_node)
        ast_node._children = (id_, index_expression_node if index_fold_ret is None else index_fold_ret,
                               expression_node if constant_fold_ret is None else constant_fold_ret)
    else:  # ID  DOT  ID  ASSIGN  expression
        raise NotImplementedError
        pass


def parse_expression_list(ast_node, symb_table):
    """
    expression_list :  expression_list  COMMA  expression
                    |  expression
    """
    if ast_node.type == 'expression':
        parse_expression_node(ast_node, symb_table)
    else:
        ast_node._children = traverse_skew_tree(ast_node, 'expression')
        for child in ast_node.children:
            parse_expression_node(child, symb_table)


def parse_expression_node(ast_node, symb_table):
    """
    parse expression node and constant folding&type checking at the same time
    expression :  expression  GE  expr
               |  expression  GT  expr
               |  expression  LE  expr
               |  expression  LT  expr
               |  expression  EQUAL  expr
               |  expression  UNEQUAL  expr
               |  expr

    """
    # 即便是 expr node, 也会建一个 expression 节点，也就是保证了 expression 节点一定出现
    children = ast_node.children
    if len(children) == 1:  # expr node
        expr_val = parse_expr_node(children[0], symb_table)
    else:
        # TODO traverse skew tree first
        # ast_node._chilren = traverse_skew_tree(ast_node, [
        #     'expr', 'term', ''
        # ])
        left_expression_child, bool_op, right_expr_child = ast_node.children
        # TODO: add const folidng support
        expression_val = parse_expression_node(left_expression_child, symb_table)
        expr_val = parse_expr_node(right_expr_child, symb_table)

    return constant_folding(ast_node, symb_table)


def parse_expr_node(ast_node, symb_table):
    """
    parse expr node
    expr :  expr  ADD  term
         |  expr  SUBTRACT  term
         |  expr  kOR  term
         |  term
    前三种情况会建一个 expr node, 最后一种情况直接是 term node
    """
    # TODO: add constant folding support
    if ast_node.type.startswith('expr'):  # expr node
        left_expr_child, right_term_child = ast_node.children
        expr_val = parse_expr_node(left_expr_child, symb_table)
        term_val = parse_term_node(right_term_child, symb_table)
    else:  # term node
        term_val = parse_term_node(ast_node, symb_table)


def parse_term_node(ast_node, symb_table):
    """
    parse term node
    term :  term  MUL  factor
            |  term  kDIV factor
            |  term  DIV  factor
            |  term  kMOD  factor
            |  term  kAND  factor
            |  factor
    最后一种情况直接是 factor node
    """
    if ast_node.type.startswith('term'):
        left_term_child, right_factor_child = ast_node.children
        term_val = parse_term_node(left_term_child, symb_table)
        factor_val = parse_factor_node(right_factor_child, symb_table)
    else:  # factor node
        factor_val = parse_factor_node(ast_node, symb_table)


def parse_factor_node(ast_node, symb_table):
    """
    return None if not const-foldable
    factor  : ID  LP  args_list  RP
            | SYS_FUNCT  LP  args_list  RP   (factor-func node)
    factor  : ID  LB  expression  RB  (factor-arr node)
    factor :  ID  (str)
           |  SYS_FUNCT  (str)
           |  const_value  (const_value node)
           |  kNOT  factor  (factor node)
           |  SUBTRACT  factor  (factor node)
    factor : LP  expression  RP (expression node) 加了括号代表了优先级而已
    factor : ID  DOT  ID (factor-member node)
    """
    if not isinstance(ast_node, Node):  # ID / SYS_FUNCT
        if ast_node in SYS_FUNC:  # sys func
            raise NotImplementedError('sys func: {} is not supported currently'.format(SYS_FUNC))
        else:  # ID
            # must be const value or variable value
            ret_val = symb_table.chain_look_up(ast_node)
            if ret_val is None:
                raise Exception("`{}` is not a const or variable or func".format(ast_node))
            else:
                if ret_val.type == 'const':
                    const_val = ret_val.value['const_val']
                    const_type = ret_val.value['const_type']
                    return const_val, const_type
                else:  # variable
                    var_type = ret_val.value['var_type']
                    return None, var_type
    elif ast_node.type in CONST_VALUE_TYPE:  # const value / true / false / maxint
        const_val, = ast_node.children
        const_type = ast_node.type
        return const_val, const_type
        # return ConstantFoldItem(const_val, ast_node.type)
    elif ast_node.type.startswith('factor'):
        if ast_node.type == 'factor-arr':
            const_val, val_type = parse_factor_arr_node(ast_node, symb_table)
            return const_val, val_type
        elif ast_node.type == 'factor-func':
            pass
        elif ast_node.type == 'factor':  # - factor / not factor
            unary_op, right_factor_child = ast_node.children
            const_val, val_type = parse_factor_node(right_factor_child, symb_table)
            if val_type == 'char':
                raise Exception('char value `{}` is not supported for `-` op'.format(const_val))
            if const_val is not None:
                if unary_op == '-':
                    if val_type == 'sys_con':
                        const_val = ConstantFoldItem.eval_val_by_type(const_val, 'integer')
                        const_val = -const_val
                        val_type = 'integer'
                    else:  # integer / real
                        const_val = -const_val
                        # val type remains same
                else:  # not
                    if val_type != 'sys_con':  # integer / real
                        val_type = 'sys_con'
                        const_val = not ConstantFoldItem.eval_val_by_type(const_val, 'sys_con')
                    else:
                        const_val = not const_val
                # 替换孩子
                ast_node._children = (const_val,)
            else:  # 只需要根据 unary op 来改变 val_type
                if unary_op == '-':
                    if val_type == 'sys_con':
                        val_type = 'integer'
                        # val type remains same
                else:  # not
                    if val_type != 'sys_con':  # integer / real
                        val_type = 'sys_con'
            return const_val, val_type

        else:  # factor-member
            raise NotImplementedError

    else:  # LP expression RP 加了括号代表了优先级而已
        # 直接是一个 expression node
        return parse_expression_node(ast_node, symb_table)


def parse_factor_arr_node(ast_node, symb_tab):
    """
    一定不可能 const fold, 直接返回 None
    parse factor-arr node
    factor  : ID  LB  expression  RB  (factor-arr node)
    """
    arr_id, index_expression_node = ast_node.children
    # arr_id 必须定义过
    ret_val = symb_tab.chain_look_up(arr_id)
    if ret_val is None:
        raise Exception('array `{}` used before defined'.format(arr_id))
    else:
        # parse index, 判断是否越界, 只有可以 const fold 的情况，才可以完全判断越界
        const_val, val_type = parse_expression_node(index_expression_node, symb_tab)
        if const_val is not None:  # 可以 const fold
            # 检查 index type 是否正确
            index_type = ret_val.value['index_type']
            if index_type != val_type:
                raise Exception('illegal index `{}` for array `{}`'.format(const_val, arr_id))
            # 检查是否越界
            left_range, right_range = ret_val.val_query('index_range')
            if const_val < left_range or const_val > right_range:
                raise Exception('illegal index `{}` for array `{}` with index range: {}'
                                .format(const_val, arr_id, (left_range, right_range)))
            # 替换孩子
            ast_node._children = (arr_id, const_val)

            # 找到数组的类型
            arr_element_type = ret_val.value['element_type']
            return None, arr_element_type

        else:  # 不能 const fold
            # 什么都不做
            arr_element_type = ret_val.value['element_type']
            return None, arr_element_type


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
        return "%s (%s)" % (node, random.uniform(0, 10))
    return "%s (%s)" % (node.type, id(node))


class ConstantFoldItem(object):
    """
    utility class for constant folding
    """
    _type_to_func = {'integer': int, 'real': float, 'sys_con': bool, 'char': str}

    def __init__(self, val, type):
        assert type in ['integer', 'real', 'sys_con', 'char'], type
        self._val = val
        self._type = type

    @staticmethod
    def eval_val_by_type(val, type):
        return ConstantFoldItem._type_to_func[type](val)

    @property
    def val(self):
        return self._type_to_func[self._type](self._val)

    @property
    def type(self):
        return self._type

    def __le__(self, other):
        if isinstance(other, ConstantFoldItem):
            other = other.val
        return self.val <= other

    def __ge__(self, other):
        if isinstance(other, ConstantFoldItem):
            other = other.val
        return self.val >= other

    def __lt__(self, other):
        if isinstance(other, ConstantFoldItem):
            other = other.val
        return self.val < other

    def __gt__(self, other):
        if isinstance(other, ConstantFoldItem):
            other = other.val
        return self.val > other

    def __str__(self):
        return str(self.val)

    def __add__(self, other):
        pass

