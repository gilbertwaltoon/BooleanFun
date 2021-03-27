# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 13:22:20 2021

@author: DaddyDog
"""
from peekablestream import PeekableStream

def traverse(l, tree_types=(list, tuple)):
    if isinstance(l, tree_types):
        for value in l:
            for subvalue in traverse(value, tree_types):
                yield ('\t' + str(subvalue))
    else:
        yield l

def pprint_tree(t):  
    ps = PeekableStream(t);
    nps = ps.move_next()
    while nps is not None:
       # print(nps)
        tv = PeekableStream(traverse(nps))
        ntv = tv.move_next()
        while ntv is not None:
           # print(ntv)
            ntv = tv.move_next()
        nps = ps.move_next()

   # tt = list(t)
   # print(tt)
   # ttt = list(traverse(tt))
   # print(ttt)
 #   print(t) 
   # for _ in ttt:
     #       print(_)

# def pprint_tree(p):
#     l = traverse(p)
#     n = next(l)
#     while n is not None:
#         print(n)
#         n = next(l)
#     # print(l)
#     # for i in l:
#     #     print(i)
