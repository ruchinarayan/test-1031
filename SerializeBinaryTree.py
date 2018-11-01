#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 21:56:46 2018

@author: ruchinarayan

Coding Exercise 2: Serialize a Binary Tree

"""

import pickle

class Node:

    def __init__(self,val):
        self.left = None
        self.right = None
        self.rootid = val

    def setNode(self,val):
        self.rootid = val

    def getNode(self):
        return self.rootid

    def rightInsert(self, val):
        if self.right == None:
            self.right = Node(val)
        else:
            tree = Node(val)
            tree.right = self.right
            self.right = tree

    def leftInsert(self, val):
        if self.left == None:
            self.left = Node(val)
        else:
            tree = Node(val)
            tree.left = self.left
            self.left = tree

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

def printBinaryTree(tree):
    if tree != None:
        print(tree.getNode())
        printBinaryTree(tree.getLeftChild())
        printBinaryTree(tree.getRightChild())
        
binaryTree = Node(1)
binaryTree.leftInsert(2)
binaryTree.rightInsert(3)
binaryTree.rightInsert(5)
binaryTree.leftInsert(4)

pass

def serialize_tree(root_node):
    """
    Serializes a tree from top to bottom, left to right to a list of values

    Parameters
    ----------
    root_node : root node of a binary tree
        The tree is not ordered or balanced, it's just a binary tree
        Example:
            1
           / \
          2   3
         / \ / \
           4 2
      
    Returns
    -------
    serial_tree :  A list of serialized values
        Example: [1,2,3,None,4,2,None]
    """
    serializeToFile  = open("binarytree.pickle.txt","wb")
    pickle.dump(root_node, serializeToFile )
    serializeToFile .close()

    deserializeFromFile  = open("binarytree.pickle.txt", "rb")
    root_node_out = pickle.load(deserializeFromFile )
    deserializeFromFile .close()

    printBinaryTree(root_node_out)


print ("Output Binary Tree")
serialize_tree(binaryTree)
    