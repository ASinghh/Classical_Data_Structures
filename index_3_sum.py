# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 11:48:20 2022

@author: Ashutosh_Singh8
"""
from collections import defaultdict
nums = [-1,0,1,2,-1,-4]
ct = defaultdict(int)
for i in range(len(nums)):
    ct[nums[i]] +=1
            
def sumfind(val, arr,excl):
    dct = ct.copy()
    dct[excl] = 0
    #print(dct,ct)
    ret = []
                
    for i in range(len(arr)):
        if arr[i] !=val/2 and dct[val-arr[i]]!=0  and dct[arr[i]] !=0:
            ret.append([arr[i],val-arr[i]]) 
            dct[val-arr[i]] = 0
        if arr[i] ==val/2 and dct[arr[i]]>=2 and dct[arr[i]] !=0:
            print(dct[arr[i]], arr[i])
            ret.append([arr[i],arr[i]]) 
            dct[val-arr[i]] = 0
    return ret

final_ret =[]
ddt = ct.copy()
for i in range(len(nums)):
    ret =[]
    if ddt[nums[i]] !=0:
        ddt[nums[i]] ==0
        ret = sumfind(0-nums[i], nums, i)
    for j in ret:
        final_ret.append(j+[nums[i]])  
                
print(final_ret)