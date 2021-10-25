# Problem:Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
# Then print the respective minimum and maximum values as a single line of two space-separated long integers.

#!/bin/python3

import math
import os
import random
import re
import sys


#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    ordered_arr = sorted(arr) #sort array in ascending order
    min_sum = sum(ordered_arr[0:4]) #Find min sum of four integers 
    max_sum = sum(ordered_arr[1:5]) #Find max sum of four integers
    print (str(min_sum) + " " + str(max_sum)) #Print min sum and max sum in a single line, space sparated

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
