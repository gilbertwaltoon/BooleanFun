# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 09:23:00 2021

@author: DaddyDog
"""

import unittest
import sys
sys.path.append("../")

from test_func import test_func

class TestClass(unittest.TestCase):
    def test_ImportFromFile(self):
        self.assertEqual(test_func(1,1),2)
        self.assertEqual(test_func(1,1),3)
        
if __name__ == '__main__':
    unittest.main()