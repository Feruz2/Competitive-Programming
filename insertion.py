#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
# 

def insertionSort1(n, arr):
    # Write your code here
    last=arr[n-1]
    is_done=False
    for i in range((n-2),-2,-1):
        
        if(last<arr[i]):
            arr[i+1]=arr[i]
            if(i==-1):
                arr[i+1]=last
        
        else:
            arr[i+1]=last
            is_done=True
            
            
            
        for num in arr:
            print(num, end =" ")
        print()  
        if(is_done):
            break

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
