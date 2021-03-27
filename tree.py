# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 15:14:38 2021

@author: DaddyDog
"""

from treenode import TreeNode
import sys


class Tree:
  '''
    The tree maintains a double linked list.
    Nodes should list their parents, but do not need to 
    explictly update the children lists of those parents
  '''
  def __init__(self, root = None, name = None):
      self.tree = {}        
      if (root is not None) and (not isinstance(root, TreeNode)):
          raise Exception("Root must be None or object of class TreeNode")
      else:
          self.name = name
          self.tree[root.name] = root
          self.root = root
          self.last_added = root
      
  def set_root(self, root):
      if not isinstance(root, TreeNode):
          raise Exception("Root must be an object of type TreeNode")
      elif root in self.tree:
          raise Exception('Root already exits in the tree')
      else:
          self.tree['root'] = root
          self.root = root
          self.last_added = root
   
  def add_node(self, node):
      if not isinstance(node, TreeNode):
          raise Exception("add_node argument must be an object of type TreeNode")
      elif node in self.tree:
          raise Exception("Node already exists in the tree")
      elif node.parents == []:
          raise Exception("For safety, parents list should be non-empty. This could be modified in future")
      else:
          self.tree[node.name] = node
          self.last_added = node
         # parents_to_inform = []  
          for parent_node in node.parents:   
              if node not in parent_node.children:  
                   l = [_ for _ in parent_node.children] 
                   l.append(node)
                   parent_node.children = l
       
                
       
        
       
  # def insert_node(self, node, upper, lower):
  #     if not [isinstance(x,TreeNode) for x in (node,upper,lower)]:
  #         raise Exception("insert_node args must be objects of type TreeNode")
  #     else:
  #         self.tree[upper.name].children.delete(lower)
  #         self.tree[upper.name].childen.append(node)
  #         self.tree[lower.name].parent.delete(upper)
  #         self.tree[lower.name].parent.append(node)
 
        
  def __str__(self, level = 0, node = None):
      if level == 100:
          sys.exit("tree __str__ reached recursion limit of level =" + str(level))
      if level == 0:
          node = self.root   
      ret = "\t"*level + node.name +'\n'
      for child in node.children:
          ret += self.__str__(level = level+1, node = child)
      return ret
  
    
  #def __repr__(self):
   #   return '<tree node representation>'