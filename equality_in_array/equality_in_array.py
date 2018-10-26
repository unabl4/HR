# https://www.hackerrank.com/challenges/equality-in-a-array/problem

#!/bin/python3

# Complete the equalizeArray function below.
def equalizeArray(arr):
    f = {}
    for n in arr:
        f[n] = f.get(n,0)+1
        
    m = max(f, key=lambda x: f[x])
    return sum(f[i] for i in f if i != m)

# ---

n = int(input())
arr = list(map(int, input().rstrip().split()))

result = equalizeArray(arr)
print(result)
