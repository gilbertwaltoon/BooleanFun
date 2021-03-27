# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 10:52:14 2021

@author: DaddyDog
"""
import logging
logger = logging.getLogger(__name__)

from classic_lexer import classic_lexer
from peekableliststream import PeekableListStream


def classic_parser(l):
    '''
    The Classic Right-recursive Arithmetical grammar parser
    p111 Engineering A Compiler, Cooper & Torczan
    
    Run-with Example:
    -----------------
    classic_parser(classic_lexer('x+2*(3/y)')
    '''
    logging.debug("Starting classic_parser")
    pl = PeekableListStream(l)
    pl.move_next()
  
    def _expr():
        # _expr -> _term _expr2
        logging.debug("in expr()")
        if _term():
            return _expr2()
        else: 
            raise Exception("_term returned False in _expr()")
        
    def _expr2():
        # _expr2 -> + _term _expr2
        # _expr2 -> - _term _expr2
        logging.debug('in expr2 with pl.current %s' % str(pl.current))
        if pl.current[0] in ['+', '-']:
            pl.move_next()
            if _term():
                return _expr2()
            else:
                raise Exception("_term() returned False in _expr2()")
        elif pl.current[0] in [')', None]:
            # _expr2 -> eps
            return True
        else:
            raise Exception("_expr2 failed")

    
    def _term():
        # _term -> _factor _term2
        logging.debug("in term")
        if _factor():
            return _term2()
        else:
            raise Exception("_factor() returned False in _term()")
    
    def _term2():
        # _term2 -> * _factor _term2
        # _term2 -> / _factor _term2
        logging.debug("in term2 with pl.current = %s " % str(pl.current))
        if pl.current[0] in ['*', '/']:
            pl.move_next()
            if _factor():
                return _term2()
            else:
                raise Exception("_factor() returned False in _term2()")
        else: 
            if pl.current[0] in ['+', '-', ')', None]:
                # _term2 -> eps, *, /
                return True
            else:
                raise Exception('Expected +.-,) or None in _term2()')
                
    def _factor():
       # _factor ->  ( Expr )
       logging.debug("in factor with pl.current %s"% str(pl.current))
       if pl.current[0] == '(':
           pl.move_next()
           if not _expr():
               raise Exception("_expr returned False in _factor()")
           if pl.current[0] != ')':
               raise Exception("_factor() expected )")
           pl.move_next()
           return True
       elif pl.current[0] in ['num','var']:
           pl.move_next()
           logging.debug('factor returning true')
           return True
       else:
           raise Exception("_factor() failed")
      
  
    if _expr():
        if pl.move_next()[0] is None:
            return True
        else:
            raise Exception("_expr() returned with tokens still outstanding")
   
   

#def main():
#    logging.basicConfig(filename='./logs/classic_parser.log', encoding='utf-8', \
#                        filemode = 'w', level=logging.DEBUG)
#    print(classic_parser(classic_lexer('x+2*(3/y)')))
#    logging.shutdown()

    
if __name__ == '__main__':
    main()