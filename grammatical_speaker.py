# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 09:13:50 2021

@author: DaddyDog
"""
import logging
import random
from grammars import Classic_rrec_expr_grammar, Recurse_from_enum

class Grammatical_speaker:
    '''see Unittest for examples of usage
    '''
    
    def __init__(self, grammar = Classic_rrec_expr_grammar(), ran_seed = None ):
        '''
        Parameters
        ----------
        grammar : object of class grammar, optional
            DESCRIPTION. The default is Classic_rrec_expr_grammar().
        ran_seed : TYPE, optional
            DESCRIPTION. Set to integer to force reproducible 
                         behaviour for test purposes. The default is None.

        Returns
        -------
        None.

        '''
        self.grammar = grammar
        self.ran_seed = ran_seed 
        random.seed(a=self.ran_seed)
          
    def _get_rule(self, key = "random", choice = "random"):
        '''
        Returns the rule[rule][choice] from the grammar as a key value pair
        select_rule = "random" will return a rule at random
        (choice is ignored and treated as random if rule = "random") 
        '''
        if key == "random":
            key = random.choice(self.grammar.non_terms)
            
        if choice == "random":
            choice = random.choice(self.grammar.rules[key])
        else:
            choice = self.grammar.rules[key][choice]        
        return key, choice

        
    def _find_nxt_non_term(self, sent_form):
        ''' 
        Test whether any non-terminal occurs in a sentitial form
        Makes use of the Recurse_from_enum(eration) of the Grammar to
        decide from which end of the sentential form to begin searching
        
        Args
        ----
            sent_form = list ["_expr", "foo123"]        
        Returns
        -------
            (index, the-non-terminal-found) e.g. (-1,"_expr")
            
        '''   
        if self.grammar.recurse_from == Recurse_from_enum.RIGHT:
            l = len(sent_form)
            sent_form = reversed(sent_form)
        for idx,term in enumerate(sent_form):
           if term in self.grammar.rules:
               if self.grammar.recurse_from == Recurse_from_enum.RIGHT:
                   return l-idx-1, term # correct idx if traversing from right
               else:
                   return idx, term
        return None,None   

    def _replace(self, idx, amenda, lst):
        '''
        Parameters
        ----------
        idx : integer, 
            index of the element in the list to replace 
        amenda : list  
            list of new elements to insert in lst
        lst : list
            the list to be amend

        Returns
        -------
            None. (the function amends the list, lst, in place)
        '''
        lst[idx:idx] = amenda
        del lst[idx+len(amenda)]
        return 
    
    def say_sentence(self, max_iters = 10):
        sent_form = self.grammar.start
        for i in range(0, max_iters): # Stop after finite sentence recursions 
            # Find the next non-terminal to replace with its rule
           idx, non_term = self._find_nxt_non_term(sent_form)
           if non_term == None: 
               return ' '.join(sent_form), sent_form
           else:
               # Find the rule for the given non-term
               # If there are several, pick one at random
               replacement = self._get_rule(non_term, "random")[1]
               # Perform the replacement
               self._replace(idx, replacement, sent_form)  
        return ' '.join(sent_form), sent_form
        