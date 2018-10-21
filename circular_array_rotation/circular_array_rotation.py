# https://www.hackerrank.com/challenges/circular-array-rotation/problem

#!/bin/python3

# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):
    v = []
    n = len(a)
    for q in queries:
        i = (q-k) % n
        v.append(a[i])
        
    return v

# ---

n,k,q = map(int, input().split())
a = list(map(int, input().rstrip().split()))
queries = []

for _ in range(q):
    queries_item = int(input())
    queries.append(queries_item)

result = circularArrayRotation(a, k, queries)
print('\n'.join(map(str, result)))
