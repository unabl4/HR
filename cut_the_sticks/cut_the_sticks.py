# https://www.hackerrank.com/challenges/cut-the-sticks/problem

#!/bin/python3

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    c = len(arr)
    f = {} # freq
    for a in arr:
        f[a] = f.get(a,0)+1
    
    l = [] # lengths
    v = sorted(f.items())
    for i in v:
        l.append(c)
        c -= i[1]
        
    return l
        
# ---

n = int(input())
arr = list(map(int, input().rstrip().split()))
result = cutTheSticks(arr)
print('\n'.join(map(str, result)))
