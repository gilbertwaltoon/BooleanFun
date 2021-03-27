# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 20:20:16 2021

@author: DaddyDog
"""


class Node():
    def __init__(self, parents = [], children = []):
        self.children = children
        self.parents = parents
    
class Tree():
    def __init__(self):
        self.nodes = []
        
    def __add__(self, node):
        self.nodes.append(node)
        for p in node.parents:
            if node not in 


def main():
    node1 = Node()
    node2 = Node(children = [node1]) # node 1 doesn;t know yert it's a parent
    