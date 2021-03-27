# -*- coding: utf-8 -*-
"""
Created on Sat Mar  6 13:09:15 2021

@author: DaddyDog
"""
import logging
import random

class sheep_grammar:
    '''
    run the module sheep_noises.py to see example
    
    self.rules is a dictionary of non-terminals (demarked by leading _ )
    to a list of lists of possible choices.
    
    Example grammar
    "_sheep_noise" => "_sheep_noise" "baa"
                   |  " eats grass"
    
    is represented by {"_sheep_noise"[["_sheep_noise","baa"],["baa"],["_eats"]}
    
    '''
    
    def __init__(self, name, ):
        self.name = name
        self.rules = {"_sheep_noise":[["_sheep_noise","baa"],["baa"],["_eats"]]\
                      , "_eats":[["munch"],["_sheep_noise", "munch" ]]}
        self.start = ["_sheep_noise"]
        self.allowed_non_terms = list(self.rules.keys())
        
    def _nxt(self,lhs):
        if lhs is None:
             possible_non_term = self.start[0]            
        else:
            possible_non_term = lhs[0] #Examine leftmost item
        if possible_non_term not in self.allowed_non_terms:
            return None
        else:
            non_term = possible_non_term
            r = random.choice(self.rules[non_term])
            return r
        
    def talk_to_me(self, retort = 'says'):
        lhs = self._nxt(None)
        sent = ''
        while (lhs != None):
         #   print("self._nxt returned", lhs)
            for i in lhs:
              if i[0] != '_':
               #  print("joining ", lhs[-1]," onto ", sent)
                 sent = ''.join([sent,' ', lhs[-1]])
                 logging.debug("sent is now %s", sent)
            lhs = self._nxt(lhs)  
        logging.debug("returning %s", ''.join([self.name, ' says ', sent]))
        return ''.join([self.name, ' ', retort,  ' ', sent])

        
