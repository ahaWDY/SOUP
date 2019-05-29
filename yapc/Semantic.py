# -*- coding: utf-8 -*-
# File: Semantic.py
# data struct and utility func for semantic analysis
# semantic 在做的事情其实就是生成 symbol table, 我们之前有生成一个简单的初始 symbol table
from AST import *
from SymbolTable import *
import copy





class SemanticAnalyzer(object):
    """
    static semantic analysis
    """
    def __init__(self, root_node):
        assert isinstance(root_node, Node), type(root_node)
        self._ast = root_node
        self._symb_tab = SymbolTable()

    @property
    def symbol_table(self):
        return self._symb_tab

    @property
    def abstract_syntax_tree(self):
        return self._ast

    def analyze(self):
        """
        semantic analysis interface
        currently 1 scope, 2 pass, 1th pass is done in __init__
        So basically, this func will bind values to the variable
        影响 value 值的语句，只有 assignment_statement
        但是 func, procedure 的值不方便直接做推断，这里先通通假设没有 func / procedure
        if 语句也会影响啊。。。我晕了，看看一开始的那个 c++ 代码吧
        :return:
        """
        self._traverse_tree_and_fill_tab(self._ast)

    def _insert(self, key, val):
        return self._symb_tab.insert(key, val)

    def _lookup(self, key):
        return self._symb_tab.lookup(key)

    def _delete(self, key):
        return self._symb_tab.delete(key)

    def _traverse_tree_and_fill_tab(self, root_node):
        if isinstance(root_node, Node):

            if root_node.type == 'const_expr_list':

                """ const declaration """

                # flatten the sub tree

                root_node._children = traverse_skew_tree(root_node, 'const_expr')

                for child in root_node.children:
                    id_, const_val_node = child.children
                    const_val, *_ = const_val_node.children
                    # TODO: use enum
                    symb_tab_item = SymbolTableItem('const', const_val)
                    is_conflict, ret_val = self._insert(id_, symb_tab_item)
                    if is_conflict:
                        raise ConflictIDError(id_, ret_val)

            elif root_node.type == 'var_decl_list':

                """ variable declaration """

                # flatten var_decl

                root_node._children = traverse_skew_tree(root_node, 'var_decl')

                for child in root_node.children:
                    flatten_name_list, symb_tab_item = parse_var_decl_from_node(child)

                    # insert (name, type) in symbol table
                    for id_ in flatten_name_list:
                        is_conflict, ret_val = self._insert(id_, symb_tab_item)
                        if is_conflict:
                            raise ConflictIDError(id_, symb_tab_item)

            elif root_node.type == 'type_decl_list':

                """ type declartion """

                # flatten type definitions
                root_node._children = traverse_skew_tree(root_node, 'type_definition')

                for child in root_node.children:
                    # parse type_definition
                    type_, id_, *attributes = parse_type_definition_from_type_node(child)

                    if type_ == 'alias':
                        # check whether the alias type exist
                        type_alias = attributes[0]
                        ret_val = self._lookup(type_alias)
                        if not ret_val:
                            raise Exception('type alias: `{}` used before defined'.format(type_alias))
                        symb_tab_item = copy.deepcopy(ret_val)

                    elif type_ == 'sys_type':
                        sys_type = attributes[0]
                        symb_tab_item = SymbolTableItem('sys_type', {'sys_type': sys_type})

                    else:  # array type
                        index_type, element_type, left_val, right_val = attributes
                        symb_tab_item = SymbolTableItem('arr_var',
                                                        {'index_type': index_type,
                                                         'index_range': (left_val, right_val),
                                                         'element_type': element_type})

                    # insert into symbol table
                    is_conflict, ret_val = self._insert(id_, symb_tab_item)

                    if is_conflict:
                        raise ConflictIDError(id_, symb_tab_item)
            else:
                for child in root_node.children:
                    self._traverse_tree_and_fill_tab(child)

        else:
            return
