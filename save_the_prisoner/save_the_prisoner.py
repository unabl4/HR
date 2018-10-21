# https://www.hackerrank.com/challenges/save-the-prisoner/problem

#!/bin/python3

# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    return (((s-1)+m-1) % n)+1

# ---

t = int(input())
for _ in range(t):
    n,m,s = map(int, input().split())
    result = saveThePrisoner(n, m, s)
    print(result)
