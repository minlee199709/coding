
#Given a time in 12-hour AM/PM format, convert it to military (24-hour) time
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    hour = int(s[0:2]) # get hour
    time = s [8:9] # Determine if time is PM or AM
    if time == 'P' or time == 'p': # If time is in PM
        if hour != 12: # if hour is not 12
            hour = int(hour) + 12 # hour + 12 hours to get 24 hour format
        else:# if hour is 12
            hour = hour # keep hour as 12
        return (str(hour) + s[2:8])
    else: # If time is not in PM
        if hour == 12: # if hour is 12
            return ("00" + s[2:8]) # return 00 instead of 12 to get 24 hour format
        else: # if hour is not 12
            return (s[:8]) # return time without AM
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)
    fptr.write(result + '\n')
    fptr.close()
