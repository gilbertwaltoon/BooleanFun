# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 20:13:58 2021

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

def boolean_lexer(chars_iter):
    chars = PeekableStream(chars_iter)
    while chars.next is not None:
        c = chars.move_next()
        if c in " \n": 
             pass           # Ignore whitespace
        elif c in "()":
            yield([c,''])
        elif c in "*+!":
            yield([c,''])
        elif re.match("[_a-zA-Z]", c):
            yield(['var', _scan(c, chars, "[_a-zA-Z0-9]")])
        elif re.match("[0-9]", c):
            yield(['num', _scan(c, chars, "[0-9]")])
        else:
            raise Exception("Unrecognised character ", c)
            