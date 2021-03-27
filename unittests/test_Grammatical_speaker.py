# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 10:11:23 2021

@author: DaddyDog
"""

import unittest
import sys
sys.path.append("../")

from Grammatical_speaker import Grammatical_speaker, Recurse_from_enum
from Grammars import Sheep_grammar

def printgen(i):
    return [_ for _ in i]

class TestClass(unittest.TestCase):
    def test_ImportFromFile(self):
      
      # Get speaker. By default will use the classic rec expression gramma.
      # Set an optional ran_seed to force reproducibility for unittest purposes
      gs = Grammatical_speaker(ran_seed = 2) 
     
      # ask for info. on the (default) grammar being used   
      self.assertEqual(gs.grammar.about[0:13], "The Classic R") #... only part print for unitest
      
      self.assertEqual(gs.grammar.recurse_from, Recurse_from_enum.RIGHT)
      
      # ask for non-terms
      self.assertEqual(gs.grammar.non_terms, ['_expr', '_expr2', '_term', '_term2', '_factor'])
      
      # ask for start symbol
      self.assertEqual(gs.grammar.start, ['_expr'])
      
      # ask for a "random" rule, but set the seed so that unittest is predictable
      self.assertEqual(gs._get_rule(), ('_expr', ['_term', '_expr2']))
      
      # ask for the '_expr2' rule. Since there are multiple choices we should get 0th by default
      self.assertEqual(gs._get_rule('_expr2'), ('_expr2', ["+", "_term", "_expr2"]))
      
      # ask for 2nd choice of the '_term2' rule. 
      self.assertEqual(gs._get_rule(key = '_term2', choice = 1), ('_term2', ["/", "_factor", "_term2"]))
      
      # ask for a non-existent and check raises Exception
      self.assertRaises(KeyError, lambda:gs._get_rule('_foo'))
      
      # Check whether the starting sentential form includes a non_term
      sent_form = gs.grammar.start
      self.assertEqual(gs._find_nxt_non_term(sent_form), (0,'_expr'))
      
      # Create a sentential form that includes all the grammar's non-terminals
      # and check that _find_nxt_non_term returns the right-most 
      # (as dictated by the grammar's recurse_from_enum attribute)
      sent_form = gs.grammar.non_terms
      idx = len(sent_form)-1
      self.assertEqual(gs._find_nxt_non_term(sent_form), (idx, sent_form[idx]))
      
      # Create a more complex sentential form to parse
      sent_form = gs.grammar.rules["_term2"][0] + gs.grammar.rules["_factor"][0]
      # ['*', '_factor', '_term2', '(', '_expr', ')']
      self.assertEqual(gs._find_nxt_non_term(sent_form), (4,'_expr'))
      
      # Check the case that no non-terms exist in sentential form 
      self.assertEqual(gs._find_nxt_non_term(['foo', '_bar']), (None,None))
      
      # Check ability to replace elements in a list
      l = ['a','b','c']  
      # Replace 0'th element in 'l' with x,y :
      gs._replace(0, ['x','y'], l)  # No return value. 'l' amended in-place
      self.assertEqual(l, ['x','y','b','c'])
      gs._replace(2, ['z'], l)
      self.assertEqual(l, ['x','y','z','c'])
      
      # Check we can get a sentence.
      # Since we set a gs.ran_seed above, the outcome is predictable                
      self.assertEqual(gs.say_sentence(max_iters = 5)[0], '_term + _factor / _factor _term2 _eps')
      
      # Now try with a different (left recursive) grammar
      flossy =  Grammatical_speaker(grammar = Sheep_grammar(), ran_seed = 2) 
      self.assertEqual(flossy.say_sentence()[0], 'baa baa baa baa')
        
if __name__ == '__main__':
    unittest.main()   
    