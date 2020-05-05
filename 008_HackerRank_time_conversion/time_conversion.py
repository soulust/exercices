#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    if s[0:2] == "12" and s[8::] == "PM":
        return(s[:8])
    elif s[8::] == "PM":
        t = int(s[0:2])
        t += 12
        return(str(t) + s[2:8])
    if s[0:2] == "12" and s[8::] == "AM":
        u = "00"
        return(u + s[2:8])
    elif s[8::] == "AM":
        return(s[:8])

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
