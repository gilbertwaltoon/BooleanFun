# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 15:11:15 2021

@author: DaddyDog
"""

import random

class TreeNode:
    
    def __init__(self, name = None, root = False, parents = [], children = [], data = []):
        if root is True:
            if parents != []:
                raise Exception("root cannot have a parent")
            if name == None:
                self.name = 'root'
            else:
                self.name = name
        elif name is None:
            self.name = '{:0x}'.format(random.getrandbits(128))
        else:
            self.name = name
        self.children = children
        self.parents = parents
        self.data = data
        
    def __str__(self):
        return ''.join(['Name:', self.name, '\nParents:', str(self.parents),\
                        '\nChildren:', str(self.children), '\nData:', str(self.data)])

    
    
       # ch.insert(-1, nd)
     #   self.children.insert(-1, nd)
      #  self.children.append([nd])