#!/bin/python3

import math
import os
import random
import re
import sys

from attr import asdict

#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def encryption(s):
    s = ''.join(s.split())
    row = int(math.sqrt(len(s)))
    column = row+1
    s = s.split()
    arr = [row][column]   

    for x in s:
        for i in range(row):
            for j in range(column):
                arr.append(s[i][j])

    test = ''.join(arr)
    return test
    
if __name__ == '__main__':

    s = input()

    result = encryption(s)

    print(result)
