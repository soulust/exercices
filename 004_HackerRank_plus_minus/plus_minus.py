#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    p = 0
    ne = 0 
    z = 0
    for i in range(n):
        if arr[i] > 0:
            p += 1
        if arr[i] < 0:
            ne += 1
        if arr[i] == 0:
            z += 1
    pos = (round(p/n, 6))
    print(format(pos, '.6f'))
    neg = (round(ne/n, 6))
    print(format(neg, '.6f'))
    zer = (round(z/n, 6))
    print(format(zer, '.6f'))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
