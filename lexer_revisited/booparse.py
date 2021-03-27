# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 10:53:04 2021
booparse.py
@author: DaddyDog
"""
from peekablestream import PeekableStream

class Parser:
    
    def __init__(self, tokens, stop_at):
        self.tokens = tokens
        self.stop_at = stop_at
        
    def next_expression(self, prev):
        print("next_expression called with prev=",prev)
        self.fail_if_at_end(";")
        typ, value = self.tokens.next
        print("fetching token for analysis =", typ, value)
        if typ in self.stop_at:
            return prev
        self.tokens.move_next()
        if typ == 'literal' and prev is None:
            return self.next_expression((typ, value))
        elif typ == 'binary':
            nxt = self.next_expression(None)
            return self.next_expression(('binary', value, prev, nxt))
        elif typ == 'unary':
            nxt = self.next_expression(None)
            return self.next_expression(('unary', value, nxt))
        elif typ == '(':
            args = self.multiple_expressions(";",")")
            return self.next_expression(('term', prev, args))
        else:
            raise Exception("Unexpected token:" + str((typ,value)))
            
        
    def multiple_expressions(self, sep, end):
        ret = []
        self.fail_if_at_end(end)
        typ = self.tokens.next[0]
        if typ == end:
            self.tokens.move_next()
        else:
            arg_parser = Parser(self.tokens, (sep, end))
            while typ != end:
                p = arg_parser.next_expression(None)
                if p is not None:
                    ret.append(p)
                typ = self.tokens.next[0]
                self.tokens.move_next()
                self.fail_if_at_end(end)
        return ret
     
        
    def fail_if_at_end(self, expected):
        if self.tokens.next is None:
            raise Exception("Hit end of file - expected '%s'." % expected)
 

def parse(tokens_iterator):
    parser = Parser(PeekableStream(tokens_iterator), ";")
    while parser.tokens.next is not None:
        p = parser.next_expression(None)
        if p is not None:
            yield p
        parser.tokens.move_next() 