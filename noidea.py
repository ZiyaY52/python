
import numpy as np
arr = np.array([])


n,m = input().split()

A = np.array([])
B = np.array([])
happiness = 0

arr = list(map(int, input().split()))
    
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for x in arr:
    if x in A:
        happiness = happiness+1
    if x in B:
        happiness = happiness-1

print(happiness)

    
