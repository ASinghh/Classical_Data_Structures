# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 11:45:16 2022

@author: Ashutosh_Singh8
"""
from collections import defaultdict
def sumfind(val, arr,excl): #excl is which index to exclude
    dct = defaultdict(list)
    ret = []
    for i in range(len(arr)):
        if i!=excl:
            dct[arr[i]].append(i)
                
    for i in range(len(arr)):
        if arr[i] !=val/2 and len(dct[val-arr[i]])!=0 and i!=excl:
            for j in dct[val-arr[i]]:
                ret.append([arr[i],arr[j]]) 
                dct[arr[i]] = []
        if arr[i] ==val/2 and len(dct[arr[i]])>=2 and i!=excl:
            dct[arr[i]].remove(i)
            for j in (dct[arr[i]]):
                ret.append([arr[i],arr[j]]) 
    return ret