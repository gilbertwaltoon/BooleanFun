# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 09:51:17 2021

@author: DaddyDog
"""

import unittest
import sys
sys.path.append("../")

from sheep_lexer import sheep_lexer

class TestClass(unittest.TestCase):
    def test_ImportFromFile(self):
        
        # Check lexer recognises 'baa' as a _sheep_noise
        self.assertEqual(sheep_lexer('baa'), [['_sheep_noise', 'baa']])
        self.assertEqual(sheep_lexer('baa baa'), [['_sheep_noise', 'baa'],['_sheep_noise', 'baa']]) 
        self.assertEqual(sheep_lexer('baabaa'), [['_sheep_noise', 'baa'],['_sheep_noise', 'baa']])
        self.assertEqual(sheep_lexer('baa  baa'), [['_sheep_noise', 'baa'],['_sheep_noise', 'baa']])
   
        # check error trapping
        self.assertRaises(Exception, lambda:sheep_lexer('b'))
        self.assertRaises(Exception, lambda:sheep_lexer('ba'))
        self.assertRaises(Exception, lambda:sheep_lexer('baa%'))
        self.assertRaises(Exception, lambda:sheep_lexer('baa ba'))
        self.assertRaises(Exception, lambda:sheep_lexer(''))
        
        
    
if __name__ == '__main__':
    unittest.main() 