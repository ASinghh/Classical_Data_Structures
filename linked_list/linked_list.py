# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



class linked_list_node:
    
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None
        
    def link_next(self,node):
        self.next = node
        
    def link_previous(self,node):
        self.previous = node
        

        
class MyLinkedList:
    
    def __init__(self, node):
        self.head = node
        self.curr = node

    def reset_curr(self):
        self.curr = self.head
        
    def get(self, index):
        i = 1
        while i <=index and self.curr.next != None:
            self.curr = self.curr.next
            i+=1
        value = -1
        if i-1 == index:
            value = self.curr.value
        self.reset_curr()
        return value
        
    def addAtHead(self, node):
        temp_node = self.head
        self.head = node
        self.head.next = temp_node
        self.reset_curr()
        
    