#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 10:34:37 2022

@author: igororlov
"""

def fact(n):
    if n == 1:
        return n
    return n * fact(n - 1)


def fib(n):
    if n >= 3:
        return fib(n - 1) + fib(n - 2)
    else:
        return 1
    
unsortedList = [4,5,2,3,6,1]
   
def mergeSort(arr):
    if len(arr) == 1:
        #base case
        return arr
    else:
        a = arr[:len(arr)//2] # left side of the arr
        b = arr[len(arr)//2:] # right side of the arr
        
        a = mergeSort(a)
        b = mergeSort(b)
        
        c = [] #ordered list of a and b arrays
        
        i = j = 0
        
        while i < len(a) and j < len(b):
            #i iterates over a array (left side)
            #j iterates over b array (right side)
            
            if a[i] < b[j]:
                c.append(a[i]) #append current val from a array
                i += 1  # increment i pointer
            else:
                c.append(b[j]) #append current val from b arr
                j += 1 # incement j pointer
                
        #once one the loop ends, add the rest of the arrays
        #to c
        
        c += a[i:]
        c += b[j:]
        
    return c
        
