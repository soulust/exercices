#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    count = 0
    for i in reversed(range(n)):
        r = (" "* (i))
        print(r + "#" + "#"*count + r)
        count = count + 2
    print((" "*int(count/4) + "|" + " "*int(count/4) + "|" + " "*int(count/4) + "\n")*int(n/2))    

if __name__ == '__main__':
    n = int(input())

    staircase(n)
