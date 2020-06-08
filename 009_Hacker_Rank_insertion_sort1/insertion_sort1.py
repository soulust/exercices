#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    for i in range(1, n):
        cV = arr[i]
        position = i
        while position>0 and arr[position-1]>cV:
            arr[position]=arr[position-1]
            position = position-1
            print(*arr)
        arr[position]=cV
    print(*arr) 

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
