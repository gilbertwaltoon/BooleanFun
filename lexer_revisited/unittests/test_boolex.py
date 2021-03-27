# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 10:11:23 2021

@author: DaddyDog
"""

import unittest
import sys
sys.path.append("../")

from boolex import lex

def printgen(i):
    return [_ for _ in i]

class TestClass(unittest.TestCase):
    def test_ImportFromFile(self):
        
        l = lex("a")
        self.assertEqual(printgen(l), [('term', 'a')])
    
        l = lex("a*b")
        self.assertEqual(printgen(l), [('term', 'a'), ('binary','*'), ('term','b')])
        
        l = lex("!a")
        self.assertEqual(printgen(l), [('unary','!'),('term', 'a')])
        
        l = lex("¬a")
        self.assertEqual(printgen(l), [('unary','¬'),('term', 'a')])
        
        l = lex("a->b")
        self.assertEqual(printgen(l), [('term', 'a'), ('binary','->'), ('term','b')])
        
        l = lex("a<->b")
        self.assertEqual(printgen(l), [('term', 'a'), ('binary','<->'), ('term','b')])
        
        l = lex("a1+b")
        self.assertEqual(printgen(l), [('term', 'a1'), ('binary','+'), ('term','b')])
        
        l = lex("a=b")
        self.assertEqual(printgen(l), [('term', 'a'), ('=',''), ('term','b')])
        
        
if __name__ == '__main__':
    unittest.main()