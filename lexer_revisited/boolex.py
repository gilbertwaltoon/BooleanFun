# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 09:49:22 2021

boolex

@author: DaddyDog
"""

import re

from peekablestream import PeekableStream
    

def _scan(first_char, chars, allowed):
    ret = first_char
    p = chars.next
    while p is not None and re.match(allowed, p):
        ret += chars.move_next()
        p = chars.next
    return ret

def _scan_string(delim, chars):
    ret = ""
    while chars.next != delim:
        c = chars.move_next()
        if c is None:
            raise Exception("A string ran off the end of the program.")
        ret += c
    chars.move_next()
    return ret

def lex(chars_iter):
    chars = PeekableStream(chars_iter)
    while chars.next is not None:
        c = chars.move_next()
        if c in " \n" : 
            pass # ignore white space
        elif c in "()=;":
            yield(c, "") # special characters
        elif c in "!¬~":
            yield("unary", c)
        elif c in ".^+*@":  # use @ as XOR
            yield("binary", c)
        elif c in "-":  # detect implication "->"
            yield("binary", _scan(c,chars,"[>]"))
        elif c in "<":  # detect equivalence "<->
            yield("binary", _scan(c,chars,"[->]"))
        elif re.match("[a-zA-Z]",c):
            yield("literal", _scan(c,chars,"[0-9]"))
        elif c == "\t":
            raise Exception("Tab characters are not allowed.")
        else:
            raise Exception("Unrecognised character: '" + c + "'.")  
        
            
