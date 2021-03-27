# -*- coding: utf-8 -*-
"""
Created on Sun Feb 28 09:35:05 2021

Peekable Stream class

@author: DaddyDog
"""


class PeekableStream:
        
    def __init__(self, iterator):
        self.iterator = iter(iterator)
        self._fill()
        
    def _fill(self):
        try:
            self.next = next(self.iterator)
        except StopIteration:
            self.next = None
    
    def move_next(self):
        ret = self.next
        self._fill()
        return ret
    
    