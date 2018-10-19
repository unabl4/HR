# https://www.hackerrank.com/challenges/utopian-tree/problem

#!/bin/python3
from math import ceil

# Complete the utopianTree function below.
def utopianTree(n):    
    r = ceil(n/2)+1
    return 2**r-1-(n%2!=0)
    
# ---    

t = int(input())
for _ in range(t):
    n = int(input())
    result = utopianTree(n)
    print(result)
