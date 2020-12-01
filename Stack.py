#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 23:53:40 2020

@author: juan
"""

class Stack:
    def __init__(self):
        self.stack=[]
        
    #Method to add a new element to the Stack
    def add(self,e):
        if(e not in self.stack):
            self.stack.append(e)
            return True
        else:
            return False
    
    #Method to see the last element added to the Stack.
    def peek(self):
        return self.stack[-1]
    
    #Method to delete the las element added to the Stack.
    def pop(self):
        if len(self.stack)<=0:
            return("Nada para borrar.")
        else:
            return self.stack.pop();
        
hotcake= Stack()
hotcake.add("hola")
hotcake.add("Como estas")
hotcake.add("mal")
print(hotcake.peek())
hotcake.pop()
print(hotcake.peek())