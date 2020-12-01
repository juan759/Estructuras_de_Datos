#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 22:46:11 2020

@author: juan
"""
from random import *

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LikedList:
    def __init__(self):
        self.head=None
        self.length=0
    
    #Method to print the list.
    def PrintList(self):
        printval=self.head
        while printval is not None:
            print(printval.data)
            printval=printval.next
            
    #Method to add a new element to the list.
    def add(self,info):
        self.atEnd(info)
        
    #Method to add a new element at the end of the list.
    def atEnd(self,data):
        NewNode=Node(data)
        if self.head is None:
            self.head=NewNode
            return
        last=self.head
        while(last.next):
            last=last.next
        last.next=NewNode
        self.length=self.length+1
        
    #Method to add a new element at the beginning of the list.
    def atBegining(self,data):
        NewNode=Node(data)
        NewNode.next=self.head
        self.head=NewNode
        self.length=self.length+1
    
    #Method to delete a Node from the List.
    def remove(self,data):
        Head=self.head
        if(Head is not None):
            if(Head.data==data):
                self.head=Head.next
                Head=None
                return
            while (HeadVal is not None):
                if HeadVal.data == Removekey:
                    break
                prev = HeadVal
                HeadVal = HeadVal.next

        if (HeadVal == None):
            return

        prev.next = HeadVal.next
        HeadVal = None
        self.length=self.lenght-1
               
seed(56)
linked=LikedList()
linked.atBegining(4)
for i in range(4):
    linked.add(random())
    linked.add(randint(1,56))
linked.remove(4)
    
linked.PrintList()
        
        
        
        