# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 14:24:37 2021

@author: DaddyDog
"""
import sys
sys.path.append("../")

from boolex import lex
from booparse import parse
from pprint_tree import pprint_tree

print('Starting')
l = lex('a+b;')
p = parse(l)

pprint_tree(p)

    

#y = next(t)

print('Done')

#pprint_tree(p)
#print(s)


