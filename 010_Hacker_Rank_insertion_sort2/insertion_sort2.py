#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    for i in range(1, n):
        curval = arr[i]
        pos = i
        while pos>0 and arr[pos-1]>curval:
            arr[pos]=arr[pos-1]
            pos = pos-1
        arr[pos]=curval
        print(*arr)

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
