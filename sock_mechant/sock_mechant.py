# https://www.hackerrank.com/challenges/sock-merchant/problem

#!/bin/python3

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    f = {}
    for s in ar:
        f[s] = f.get(s,0)+1
    
    return sum(c // 2 for c in f.values())

n = int(input())
ar = list(map(int, input().rstrip().split()))

result = sockMerchant(n, ar)
print(result)
