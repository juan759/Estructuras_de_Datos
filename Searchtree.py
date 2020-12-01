#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 22:11:17 2020

@author: juan
"""
from random import *

class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
        
    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left==None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            elif data> self.data:
                if self.right==None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data=data
            
    def search(self,find):
        if find<self.data:
            if self.lef is None:
                return str(find)+"Not Found"
            return self.left.search(find)
        elif find>self.data:
            if self.right is None:
                return str(find)+"Not Found"
            return sefl.right.search(find)
        else:
            print(str(self.data)+"is found")
            
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

#"""
#using random() and seed()
#seed(2987897)
#root=Node(random())
#root.insert(random())
#root.insert(random())
#root.insert(random())
#root.PrintTree()
#"""
root=Node(randint(0,98))
for i in range(10):
    root.insert(randint(0,98))
root.PrintTree()
    