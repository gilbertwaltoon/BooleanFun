# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 09:23:00 2021

@author: DaddyDog
"""

import unittest
import sys
sys.path.append("../")

from boolex import lex
from booparse import parse
from pprint_tree import pprint_tree


class TestClass(unittest.TestCase):
    def test_ImportFromFile(self):
        
        l = lex('a')
        print([_ for _ in l])
        p = parse(l)
        print([_ for _ in p])
        s = pprint_tree(p)
        self.assertEqual(s,2)

        
if __name__ == '__main__':
    unittest.main()