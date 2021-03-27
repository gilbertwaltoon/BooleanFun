# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 09:34:02 2021

@author: DaddyDog
"""

import random
from treenode import TreeNode
from tree import Tree
from Grammars import *


def main():#
        print('starting')
        b = Boolean_rrec_grammar()
        p = Classic_rrec_expr_grammar()
        print(b)
        print(p)
        
    


if __name__ == '__main__':
    main()