# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 07:21:20 2021

@author: DaddyDog
"""

def _scan_baa(s, idx):
   if s[idx+1] is None:
       raise Exception("Ran out of string. Expected character after b")
   elif s[idx+1] == 'a':
       if s[idx+2] is None:
         raise Exception("Ran out of string. Expected character after ba") 
       elif s[idx+2] == 'a':
           return ['_sheep_noise', 'baa'], idx + 3;
   else:
       raise Exception("Unexpected character", s[idx])
   
def sheep_lexer(s):
    l = []
    idx = 0
    if s[idx] is None:
        raise "Expected non empty string"
    else:
        while(idx < len(s)):
         if s[idx] in " \n" : 
            idx += 1 
            pass # ignore white space
         elif s[idx] in "b":
             token, idx = _scan_baa(s, idx)
             l.append(token)
         else:
             raise Exception("Uncognised character", s[idx])    
    return l

