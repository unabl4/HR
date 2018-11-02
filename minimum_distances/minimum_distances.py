# https://www.hackerrank.com/challenges/minimum-distances/problem

#!/bin/python3

# Complete the minimumDistances function below.
def minimumDistances(a):
    d = -1 # min distance
    n = len(a)
    f = {} # indices
    for i in range(n):
        f[a[i]] = i
    
    for j in range(n):
        if a[j] in f and f[a[j]] != j:
            m = abs(j-f[a[j]])
            if d == -1:
                d = m
            else:
                d = min(d, m)
    
    return d

# ---

n = int(input())
a = list(map(int, input().rstrip().split()))
result = minimumDistances(a)
print(result)
