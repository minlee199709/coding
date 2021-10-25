#Problem: Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
#Print the decimal value of each fraction on a new line with  places after the decimal.

#!/bin/python3

import math
import os
import random
import re
import sys


# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    total_nums = len(arr)
    # Check if num in arr is positive, negative, or zero. 
    for num in arr:
        if (int(num) < 0): 
            neg += 1
        elif (int(num) > 0):
            pos += 1
        else:
            zero += 1
    print (round ((pos / total_nums),6)) # ratio of elements that are positive.
    print (round ((neg / total_nums),6)) # ratio of elements that are negative.
    print (round ((zero / total_nums),6)) # ratio of elements that are zero.
    
            
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
