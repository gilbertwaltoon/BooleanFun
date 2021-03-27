# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 11:39:30 2021

A collection of helper routines to manipulate grammars

@author: DaddyDog
"""
from grammars import *

from dogLogging import DogLogging
log = DogLogging(fname = './logs/log.txt', fmode = 'w', level = 'OFF')

 #    "_expr"   : [["_expr","+","_term"] \
  #                                  ["_expr","-","_term"],\
   #                                 ["_term"]]

def _is_lrec(nt, rule):
    for r in rule:
        if r[0] == nt:
            return True
    return False
        

def _get_alpha_beta(nt, rule):
    alpha = []
    beta = []
    for r in rule:
        if r[0] == nt:
            alpha.append(r[1:])
        else:
            beta.append(r)
    return alpha, beta

def _new_rule(nt, alpha, beta):
    rule = {}
    one = []
    two = []
    ntp = nt+str(2)
    for a in alpha:
        a.append(ntp)
        one.append(a)
    one.append(["_eps"])    
    rule[ntp] = one
    for b in beta:
        b.append(ntp)
        two.append(b)
    rule[nt] = two
    return rule

def transform(g):
    '''
    Remove indirect left recusion, 
    Fig 3.6 p103 Engineering A Compiler, Cooper & Torczan 
    '''
    nts = [_ for _ in g.rules]
    log.w('in transform with nts =' + str(nts))
    for nti in nts:
        for ntj in nts[:nts.index(nti)]:  
            log.w('In transform with i and j =' + nti + ' ' + ntj)
            # get the production nti -> [p1 | p2 |...]
            for p in g.rules[nti]:
                if p[0] == ntj:
                    log.w('found instance of Ai -> yAj for' + nti + '->' + str(p)) 
                    g.rules[nti] = g.rules[ntj]
                    log.w('replaced rule for ' + nti + "with " + str(g.rules[nti]))
        # rewrite any productions to eliminate direct left recs that depend on Ai
        if _is_lrec(nti, g.rules[nti]):
         #   log.w('calling get_alpha_beta for ' + nti)
            alpha, beta = _get_alpha_beta(nti, g.rules[nti])
            new_rule = _new_rule(nti, alpha, beta)
            del g.rules[nti]
            for k in new_rule:
                g.rules[k] = new_rule[k]
            
        
def main():
    log.w('starting')
    g = boolean_lrec_grammar()
    log.w('before')
    log.w(g.rules)
    transform(g)
    log.w('after')
    log.w(g.rules)
    log.w('Done')
    
  #  print(_get_alpha_beta('_expr', g.rules['_expr']))
  #  a,b = _get_alpha_beta('_expr', g.rules['_expr'])
  #  print(_new_rule('_expr', a, b))
   
if __name__ == '__main__':
      main()
      
    