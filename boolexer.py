# -*- coding: utf-8 -*-
"""
Created on Tue Dec 24 09:32:56 2019

boolex.py

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


def boolex(chars_iter):
    chars = PeekableStream(chars_iter)
    while chars.next is not None:
        c = chars.move_next()
        if c in " \n":              pass           # Ignore white space
        elif c in "();":            yield (c, "")  # Special characters
        elif c in "+":              yield ("dnf", c)
        elif c in ".":              yield ("cnf", c)
        elif c in "!":              yield("!","")
        elif re.match("[_a-zA-Z]", c):
            yield ("literal", _scan(c, chars, "[_a-zA-Z0-9]"))
        else:
            raise Exception("Unrecognised character: '" + c + "'.")
            
            
