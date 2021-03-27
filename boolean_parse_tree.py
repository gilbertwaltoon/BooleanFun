# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 16:10:20 2021

@author: DaddyDog
"""

from boolean_lexer import boolean_lexer
from peekableliststream import PeekableListStream
from treenode import TreeNode
from tree import Tree
from dogLogging import DogLogging
   

log = DogLogging(fname = './logs/log.txt', fmode = 'w', level = 'OFF')    

def boolean_parse_tree(l):
    ''' 

   _expr   ->  _term, _expr2
   _expr2  ->  +, _term, _expr2
    	     | _eps
   _term   ->  _value, _term2
   _term2  ->  *, _value, _term2
		     | _eps
   _value  ->  !, _factor
		     | _factor
   _factor ->  (, _expr, )
		     | num
		     | var
             
    Run-with Example:
    -----------------
    boolean_parse_tree(classic_lexer('!x+2*(3/y)')
    '''
    
    log.w("Starting boolean_parse_tree")
    pl = PeekableListStream(l)
    pl.move_next()
    rootnode = TreeNode(name = '_expr', root = True, parents = [], children = [], data = [])
    t = Tree(root = rootnode, name=l) 
    log.w(t)
   # t.add_node(rootnode)
  
    def _expr(p):
        # _expr -> _term _expr2
        log.w("in expr()")
        if p is not rootnode:
            n = TreeNode(name = '_expr', parents = [p])
            t.add_node(n)
            log.w(t)
        else:
            n = p
        if _term(n):
            log.w('in expr(), calling expr2()')
            return _expr2(n)
        else: 
            raise Exception("_term returned False in _expr()")
        
    def _expr2(p):
        # _expr2 -> + _term _expr2
        #        -> _eps
        log.w('in expr2() with pl current %s ' % str(pl.current))
        n = TreeNode(name  = '_expr2', parents = [p])
        t.add_node(n)
        log.w(t)
        if pl.current[0] == '+':
            log.w('expr2 got +')
            nn = TreeNode(name = pl.current[0], parents  = [n])
            t.add_node(nn)
            pl.move_next()
            log.w('in expr2() calling term()')
            if _term(n):
                log.w('in expr2() calling expr2()')
                return _expr2(n)
            else:
                raise Exception("_term() returned False in _expr2()")
        elif pl.current[0] in [')', None]:
            log.w('in expr2 with [),None]')
            log.w('_expr returning true')
            return True, t
        else:
            raise Exception("_expr2 failed")

    
    def _term(p):
    #_term -> _value _term2
        log.w("in term() calling factor()")
        n = TreeNode(name = '_term', parents = [p])
        t.add_node(n)
        log.w(t)
        if _value(n):
            log.w('in term')
            return _term2(n)
        else:
            raise Exception("_factor() returned False in _term()")
    
    def _term2(p):
        # _term2 -> * _value _term2
        # _term2 -> eps
        log.w("in term2 with pl.current = %s " % str(pl.current))
        n = TreeNode(name = '_term2', parents = [p])
        t.add_node(n)
        log.w(t)
        if pl.current[0] == '*':
            nn = TreeNode(name = str(pl.current[0]), parents  = [n])
            t.add_node(nn)
            pl.move_next()
            log.w('in term2() with [*,/] calling factor()')
            if _value(n):
                log.w('in term2')
                return _term2(n)
            else:
                raise Exception("_factor() returned False in _term2()")
        else: 
            if pl.current[0] in ['+', '!', ')', None]:
                # _term2 -> eps, *, /
                log.w('in _term2 with [+,-,)] -> EPS, returning True')
                return True
            else:
                raise Exception('Expected +.-,) or None in _term2()')
                
    def _value(p):
        # _value -> ! _factor
        #        -> _factor
        log.w('In value')
        n = TreeNode(name = '_value', parents = [p])
        t.add_node(n)
        log.w(t)
        if pl.current[0] == "!":
           nn = TreeNode(name = '!', parents  = [n])
           t.add_node(nn)
           pl.move_next()
           log.w('in term2() with ! calling _factor()') 
           return _factor(n)
        elif _factor(n):
            return True
        else:
            raise Exception('Expected ! in _value')
    
    def _factor(p):
       # _factor ->  ( Expr )
       log.w("in factor with pl.current %s"% str(pl.current))
       n = TreeNode(name = '_factor', parents = [p])
       t.add_node(n)
       log.w(t)
       if pl.current[0] == '(':
           nn = TreeNode(name = '(', parents  = [n])
           t.add_node(nn)
           pl.move_next()
           log.w('in factor() with ( calling expr')
           if not _expr(nn):
               raise Exception("_expr returned False in _factor()")
           if pl.current[0] != ')':
               raise Exception("_factor() expected )")
           log.w('in _factor. expr returned pl.current %s' % str(pl.current))
           nnn = TreeNode(name =  ')', parents  = [nn])
           t.add_node(nnn)    
           log.w('in factor with ), returning True')
           pl.move_next()
           return True
       elif pl.current[0] in ['num','var']:
           log.w('in factor() with [num,var]')
           nn = TreeNode(name = pl.current[0] + ',' + pl.current[1], parents  = [n])
           t.add_node(nn)
           log.w(t)
           pl.move_next() 
           log.w('factor() returning true')
           return True
       else:
           raise Exception("_factor() failed")
           
    if _expr(p = rootnode):
        if pl.move_next()[0] is None:
            log.w('Leaving')
            log.w(t)
            return t
        else:
            raise Exception("_expr() returned with tokens still outstanding")

if __name__ == '__main__':
      print(boolean_parse_tree(boolean_lexer('!(!x+!y)')))