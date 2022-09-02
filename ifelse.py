#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    if n%2==1:
        print ("Weird")
    
    if n%2==0:
        if n<=5 and n>=2:
            print ("Not weird")
        if n>=6 and n<=20:
            print("Weird")
        if n>=20:
            print("Not Weird")
