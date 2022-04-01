# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class my_tree:
    
    def __init__(self, in_arr):
        self._arr = in_arr

        
    def print_arr(self):
        print(self._arr)
        
    def add_element(self,ele):
        self._arr.append(ele)
    
    def get_parent(self, ele):
        
        if ele not in self._arr:
            print("Element not in the tree, use add function to add it to the tree")
            return
        inde = self._arr.index(ele)
        if inde == 0:
            print("this is the first node, no parent to this node")
            return
        else:    
            
            oe_test = 1-(inde%2)
            return (self._arr[int((inde -1 - oe_test)/2)],int((inde -1 - oe_test)/2))
    
 
    
    def get_children(self,ele):
        
        if ele not in self._arr:
            print("Element not in the tree, use add function to add it to the tree")
            return
        
        inde = self._arr.index(ele)
        len_arr = len(self._arr)
        
        if len_arr-1 > 2*inde +1:
            return(((self._arr[2*inde +1], 2*inde +1),(self._arr[2*inde +2], 2*inde +2)))
        
        elif len_arr-1 == 2*inde +1:
            return((self._arr[2*inde +1], 2*inde +1))
        else:
            print("this node has no children")
            return
        
        
        
        
        
        
        
    