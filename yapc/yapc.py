#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
from os import path
import time


from ply import yacc, lex
import lex_pas
from yacc_pas import parser, log

from AST import graph
from Semantic import SemanticAnalyzer
from CodeGenerator import CodeGenerator
from ErrorHandler import SemanticLogger

# test_file = 'test_yacc/simple.pas'
test_file = 'demo_test_cases/assign_demo.pas'
out_file = './yapc.out'
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('--input', help='input pascal file', default=test_file)
arg_parser.add_argument('--output', help='output intermediate code path', default=out_file)
args = arg_parser.parse_args()
start = time.clock()

if args.input:
    test_file = args.input

with open(test_file, 'r') as infile:
    data = infile.read()
SemanticLogger.info(None, 'compiling {}'.format(path.basename(test_file)))

parse_tree_root = parser.parse(data, lexer=lex.lex(module=lex_pas, debug=0), debug=log)
graph(parse_tree_root, "graphs/graph")
if parse_tree_root:
    static_semantic_analyzer = SemanticAnalyzer(parse_tree_root)
    static_semantic_analyzer.analyze()
    static_semantic_analyzer.symbol_table.to_graph("graphs/symb_tab.png")
    SemanticLogger.info(None,
                        "Find {} warnings and {} errors".format(SemanticLogger.n_warn, SemanticLogger.n_error))
    if SemanticLogger.n_error == 0:
        SemanticLogger.info(None, 'producing three address code')
        code_generator = CodeGenerator(parse_tree_root, static_semantic_analyzer.symbol_table)
        code_generator.gen_three_address_code()
        if args.output:
            out_file = args.output
            code_generator.write_file(out_file)
        else:
            _ = [print(quadruple) for quadruple in code_generator.quadruple_list]
        SemanticLogger.info(None, 'done')

end = time.clock()

SemanticLogger.info(None, 'Time elapsed: {}s'.format(end - start))

graph(parse_tree_root, "graphs/new_graph")
