# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 10:04:31 2021

@author: DaddyDog
"""

class DogLogging:
    '''
    Logging is more trouble than its worth
    '''
    
    def __init__(self, name = 'mylog', fname = './logs/log.txt', fmode = 'w'):
        self.name = name
        self.fname = fname
        self.fmode = fmode
        # open file once to check, also to delete contents if mode = w
        with open (fname, fmode):
            pass
        
    def w(self, txt, level = 'INFO'):
        with open(self.fname,'a') as fp:
            fp.write(txt)
            if level == 'INFO':
                print(txt)
                
            
            
