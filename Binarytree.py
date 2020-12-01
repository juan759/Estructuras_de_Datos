#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 20:26:42 2020

@author: juan
"""
#Class to create a singular node of a binary tree
class Node:
    
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
#Now we create a function to insert a node to a Tree
    def insert(self, data):
           if self.data:
               if data < self.data:
                   if self.left is None:
                       self.left = Node(data)
                   else:
                       self.left.insert(data)
               elif data > self.data:
                   if self.right is None:
                       self.right = Node(data)
                   else:
                       self.right.insert(data)
           else:
               self.data = data
          
    def PrintTree(self):
            if self.left:
                self.left.PrintTree()
            print( self.data),
            if self.right:
                self.right.PrintTree()
            
            
root=Node(12)
root.insert(6)
root.insert(14)
root.PrintTree()
