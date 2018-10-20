# https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem

#!/bin/python3

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    n = len(c)
    e = 100
    i = 0
    t = 0
    while not (i % n == 0 and t):
        t = 1
        e -= 1
        if c[i]:
            e -= 2
        i += k
        i %= n
    
    return e
    
n,k = map(int, input().split())
c = list(map(int, input().rstrip().split()))

result = jumpingOnClouds(c, k)
print(result)
