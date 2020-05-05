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
        count = count + 1
        print(r + "#"*count)

if __name__ == '__main__':
    n = int(input())

    staircase(n)
