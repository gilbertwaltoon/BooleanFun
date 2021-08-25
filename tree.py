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
   
                   
  def remove_and_rejoin(self, node):
      ''' delete a node, rejoining subtree below it '''
     
      nps = [_ for _ in node.parents]  # the node's parents
      ncn = [_ for _ in node.children]  # the node's children
     
      for p in nps:
          p.children.remove(node)
          p.children.extend(ncn)
     
      for c in ncn:
          c.parents.remove(node)
          c.parents.extend(nps)
         
      node.parents = None
      node.children = None
         
          
          
  def delete(self, node):
      '''
      sever connection between parent and child

      '''
      nps = [_ for _ in node.parents]
      ncn = [_ for _ in node.children]
      
      for p in nps:
          p.children.remove(node)
      
      for c in ncn:
          c.parents.remove(node)
    
      node.children = None
      node.parents = None
      
  def agglomerate(self, n, nl):
      '''
      given list of nodes nl and a preferential member of the list n
      remove all nodes expect n, joining subtrees to n

      '''
      if n not in nl:
          raise Exception('In agglomerate, node arg n must be member of node list nl')
      else:
          cn = [c for c in n.children]  # get list of n's children
          for l in nl:
              if l is n:
                  pass
              else:  # for each l
                  cl = [c for c in l.children]  # get list of l's children
                  for c in cl:
                      if c not in cn: # if child of l not a child of n, append it
                         cn.append(c)
                         cp = [p for p in c.parents]
                         cp.append(n)
                         c.parents = cp
                  self.delete(l)     
      n.children = cn
              
      
      
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