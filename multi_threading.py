# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 13:46:47 2022

@author: Ashutosh_Singh8
"""

def search(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        p1 = 0
        p2 = len(nums) -1
        while p2> p1:
            
            mid = p1+ (p2-p1)//2
            print(mid)
            print(p1)
            print(p2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                p1 = mid + 1
            else:
                p2 = mid -1
        
        return -1
    
    
