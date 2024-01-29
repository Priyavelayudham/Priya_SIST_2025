"""Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example


Return '12:01:00'.


Return '00:01:00'."""
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
    # Write your code here
    hours,minutes,secondes=map(int,s[:-2].split(':'))
    am_pm=s[-2:]
    if am_pm=='AM' and hours==12:
        hours=0
    elif am_pm=='PM' and hours!=12:
        hours+=12
    result='{:02d}:{:02d}:{:02d}'.format(hours,minutes,secondes)
    return result
s='07:05:45PM'
result=timeConversion(s)
print(result)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
