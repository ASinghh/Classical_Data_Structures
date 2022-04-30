# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 13:44:26 2022

@author: Ashutosh_Singh8
"""

def merge_sort(nums):
    if len(nums)<=1:
        return nums
    mid = len(nums)//2
    left = nums[0:mid]
    right = nums[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
    j = k = 0
   
    
    ret_arr = []
    
    while j<len(left) and k<len(right):
        if left[j]<right[k]:
            ret_arr.append(left[j])
            j+=1
        else:
            ret_arr.append(right[k])
            k+=1
    
    while j < len(left):
        ret_arr.append(left[j])
        j+=1
    while k < len(right):
        ret_arr.append(right[k])
        k+=1
        
    return ret_arr

def bubble_sort(nums):
    le = len(nums)
    if len(nums)<=1:
        return nums
    
    

    
    for i in range(le -1):
        p1 = 0
        swapped = False
        while p1 < le -i -1:
            print(p1)
            if nums[p1] > nums[p1+1]:
                nums[p1],nums[p1+1] = nums[p1+1], nums[p1]
                swapped = True
            p1 +=1
        if swapped == False:
            break

    return 
        

def selection_sort(nums):
    if len(nums)<=1:
        return nums
    
    p1 = 0 
    
    while p1<len(nums):
        minm = nums[p1]
        p2 = p1
        for i in range(p1,len(nums)):
            if nums[i]< minm:
                minm = nums[i]
                p2 = i
        nums[p2] = nums[p1]
        nums[p1] = minm
        p1+=1
    
    return

def insertion_sort(nums):
            
        for i in range(0, len(nums)):
            p1 = i
            p2 = i-1
            while p1 > 0 and nums[p2]>nums[p1]:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 = p1-1
                p2 = p2-1
        return
    

def quick_sort(nums, low, high):
    if len(nums)<=1:
        return nums
    
    p1 = low
    p2 = high -1 
    
    while p1<=p2:
        if nums[p1] >=nums[high] and nums[p2]<nums[high]:
            nums[p1], nums[p2] = nums[p2], nums[p1]
            p2 -=1
            p1 +=1
        elif  nums[p1]< nums[high] and p2<nums[high]:
            p1+=1
        
        elif  nums[p1]>= nums[high] and p2>=nums[high]:
            p2-=1
            
        else:
            p1+=1
            p2-=1
    nums[-1], nums[p1] = nums[p1], nums[-1]
    
    quick_sort(nums,0, p1-1)
    quick_sort(nums,p1+1, high)
            
                    
                
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    