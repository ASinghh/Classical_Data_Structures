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
    
    def __init(self, node):
        self.head = node
        self.curr = node
        self.node_list =[node]
        
    def get(self, index):
        i = 0
        while i <= index:
            if self.curr.next == None:
                return -1
            else:
                self.curr = self.curr.next
            i += 1
            return self.curr.value
        
    def addAtHead(self, val):
        node = linked_list_node(val)
        node.next = self.head
        self.node_list.append(node)
        self.head = node
        
    