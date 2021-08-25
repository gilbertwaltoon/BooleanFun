# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 12:39:46 2021

@author: DaddyDog
"""

import unittest
import sys

sys.path.append("../")

from tree import Tree
from treenode import TreeNode



def printgen(i):
    return [_ for _ in i]

class TestTree(unittest.TestCase):
    def test_ImportFromFile(self):
    
        # Form a root 
        myrootnode = TreeNode(name = 'myrootnode', root = True, parents = [], children = [], data = ['foo'])
       # print(myrootnode)
        
        # Form a tree with myrootnode
        t = Tree(root=myrootnode, name='mytree')
        self.assertEqual(t.name, 'mytree')
        self.assertEqual(t.root.name, 'myrootnode')
        self.assertEqual(t.last_added.name, 'myrootnode')
        
        # form a node 'one' , a child of root
        node1 = TreeNode(name = 'one', parents = [myrootnode])
        self.assertEqual(node1.parents[0].name, 'myrootnode')
        
        # add nodeone to the tree        
        t.add_node(node1)
        self.assertEqual(t.last_added.name, 'one')
        # check the root node has been auto-updated to include 'one' as one of its children
        self.assertEqual(t.root.children[0].name, 'one')
                        
        # form a second node 'two' , again a child of root
        # The tree maintains a double linked list without the
        # Nodes should list their parents, but do not need to 
        # explictly update the children lists of those parents
        node2 = TreeNode(name = 'two', parents = [myrootnode])
        self.assertEqual(node2.parents[0].name, 'myrootnode')
        # add, and check the root node has been auto-updated to now include 'one and two' its children
        t.add_node(node2)
        self.assertEqual(t.root.children[0].name, 'one')
        self.assertEqual(t.root.children[1].name, 'two')    
                    
        
        # form third node, a child of node 'two'
        node3 = TreeNode('three', parents = [node2])
        self.assertEqual(node3.parents[0].name, 'two')
        # add to tree and check 'two' is auto-updated to show 'three' as one of its children
        t.add_node(node3)
        self.assertEqual(node2.children[0].name, 'three')
        self.assertEqual(t.last_added.name, 'three')
        
        # Try adding a node with no parents (=currently not allowed for safety)
        badnode = TreeNode(name = 'badnode')
        self.assertRaises(Exception, lambda:t.add(badnode))
        
        # Test deletiong node, rejoining sub-tree below 
        # Form a subtree below 'three'
        node4 = TreeNode('four', parents = [node3])
        node5 = TreeNode('five', parents = [node3])
        node6 = TreeNode('six', parents = [node4])
        t.add_node(node4)
        t.add_node(node5)
        t.add_node(node6)
        # and delete 'three'
        t.remove_and_rejoin(node3)
        self.assertEqual([c.name for c in node2.children], ['four', 'five'])
        self.assertEqual(node4.children[0].name, 'six')
        self.assertEqual(node6.parents[0].name, 'four')
        self.assertEqual(node4.parents[0].name, 'two')
        self.assertEqual(node5.parents[0].name, 'two')
        
        
    #    print(node4.parents[0].name)
        
        print('\nN.B. Can print info on a node like this: print(node2) >>>')
        print(node2)
        
        print('\n\nN.B. Can print trees nodes a trees like this: print(t) >>> ')
      #  print(myrootnode)
        print(t)

if __name__ == '__main__':
    unittest.main()  