# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 10:04:31 2021

@author: DaddyDog
"""

class DogLogging:
    '''
    Logging is more trouble than its worth
    '''
    
    def __init__(self, name = 'mylog', fname = './logs/log.txt', fmode = 'w', level = 'OFF'):
        self.name = name
        self.fname = fname
        self.fmode = fmode
        self.level = level
        # open file once to check, also to delete contents if mode = w
        with open (fname, fmode):
            pass
        
    def w(self, t, level = 'INFO'):
        with open(self.fname,'a') as fp:
            if type(t) is not str:
                try:
                    t = t.__str__()
                except:
                    raise Exception("No __str__ method implemented on arg t in DogLogging.w(t)")
            fp.write('\n'+t+'\n')
            if self._priority_(level) >= self._priority_(self.level):
                print(t)
   
    def _priority_(self, level):
        if level == 'INFO':
            return 0
        elif level == 'DEBUG':
            return 1
        elif level == 'ERROR':
            return 2
        elif level == 'OFF':
            return 1000
        else:
            raise Exception('Debug Level not recognised in DogLogging')
        
            
            
