# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 18:23:14 2021

@author: DaddyDog
"""

from enum import Enum, unique

@unique  # ensures unique enumeration
class Recurse_from_enum(Enum):
    RIGHT = -1 # values faciliate indexing into lists
    LEFT = 0


class Grammar():
    def __init__(self):
        pass 

    def print_rules(self, rules, nonterms, name):
        s = len(name)*'-' + '\n'
        s += name +  '\n' +len(name)*'-' + '\n'
        for k in nonterms:
            ss = ''
            s += k + '-> '
            prepend = ' '
            for r in rules[k]:
                ss += prepend + ' '.join(r)
                prepend = '\n\t\t |'
            s += ss + '\n'
        return s
        

class Classic_rrec_expr_grammar(Grammar) :
    ''' '''
    def __init__(self):
        self.name = 'Classic_rrec_expr_grammar'
        self.about = "The Classic Right-recursive Arithmetical Expression " +\
             "Grammar. Fig3.4, p101 Engineering A Compiler, Cooper & Torczan"
        self.recurse_from = Recurse_from_enum.RIGHT
        self.start = ["_expr"]
        self.rules = { "_expr"   : [["_term","_expr2"]], \
                       "_expr2"  : [["+", "_term", "_expr2"],\
                                    ["-", "_term"],\
                                    ["_eps"]],\
                       "_term"   : [["_factor", "_term2"]],
                       "_term2"  : [["*", "_factor", "_term2"],\
                                    ["/", "_factor", "_term2"],\
                                    ["_eps"]],\
                       "_factor" : [["(", "_expr", ")"],\
                                    ["num"],\
                                    ["var"]]}
        self.non_terms = list(self.rules.keys())
        
    def __str__(self):
        return super().print_rules(self.rules, self.non_terms, self.name)

class Classic_lrec_expr_grammar(Grammar) :
    ''' '''
    def __init__(self):
        self.name = 'Classic_lrec_expr_grammar'
        self.about = "The Classic Left-recursive Arithmetical Expression " +\
             "Grammar. Fig3.4, p101 Engineering A Compiler, Cooper & Torczan"
        self.recurse_from = Recurse_from_enum.LEFT
        self.start = ["_expr"]
        self.rules = { "_expr"   : [["_expr","+","_term"], \
                                    ["_expr","-","_term"],\
                                    ["_term"]], \
                       "_term"   : [["_term", "*", "_factor"],\
                                    ["_term", "/","_factor"],\
                                    ["_factor"]],\
                       "_factor" : [["(", "_expr", ")"],\
                                    ["num"],\
                                    ["var"]]}
        self.non_terms = list(self.rules.keys())
        
    def __str__(self):
        return super().print_rules(self.rules, self.non_terms, self.name)
        
            


class Boolean_rrec_grammar(Grammar) :
    def __init__(self):
        self.name = 'Boolean_rrec_grammar'
        self.about = "Rrec Boolean grammar auto-generated using gramma_helpers.py" +\
            "from Fig3.27, p141 Engineering A Compiler, Cooper & Torczan"
        self.recurse_from = Recurse_from_enum.RIGHT
        self.start = ["_expr"]
        self.rules = {'_expr': [['_term', '_expr2']], \
                      '_expr2': [['+', '_term', '_expr2'], \
                                 ['_eps']], \
                      '_term': [['_value', '_term2']], \
                      '_term2': [['*', '_value', '_term2'], 
                                ['_eps']], 
                      '_value': [['!', '_factor'], \
                                 ['_factor']], \
                      '_factor': [['(', '_expr', ')'], \
                                  ['num'], ['var']]}
        self.non_terms = list(self.rules.keys())

    def __str__(self):
        return super().print_rules(self.rules, self.non_terms, self.name)
                


class Boolean_lrec_grammar(Grammar) :
    def __init__(self):
        self.name = 'Boolean_lrec_grammar'
        self.about = "Fig3.27, p141 Engineering A Compiler, Cooper & Torczan"
        self.recurse_from = Recurse_from_enum.LEFT
        self.start = ["_expr"]
        self.rules = { "_expr"   : [["_expr","+","_term"],\
                                    ["_term"]], \
                       "_term"   : [["_term", "*", "_value"],\
                                    ["_value"]],\
                       "_value"  : [["!", "_factor"], \
                                    ["_factor"]], \
                       "_factor" : [["(", "_expr", ")"],\
                                    ["num"],\
                                    ["var"]]}
        self.non_terms = list(self.rules.keys())
        
    def __str__(self):
        return super().print_rules(self.rules, self.non_terms, self.name)
  
        
        
class Sheep_grammar(Grammar) :
    ''' '''
    def __init__(self):
        self.name = 'Sheep_grammar'
        self.about = "The Sheep Grammar Engineering A Compiler, Cooper & Torczan"
        self.recurse_from = Recurse_from_enum.LEFT
        self.start = ["_sheep_noise"]
        self.rules = { 
                       "_sheep_noise" : [["baa", "_sheep_noise"],\
                                         ["baa"]]}     
        self.non_terms = list(self.rules.keys())
        
    def __str__(self):
        return super().print_rules(self.rules, self.non_terms, self.name)