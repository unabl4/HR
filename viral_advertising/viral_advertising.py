# https://www.hackerrank.com/challenges/strange-advertising/problem

#!/bin/python3

# Complete the viralAdvertising function below.
def viralAdvertising(n):
    p = 5   # population
    c = 0 # cumulative
    
    for _ in range(n):
        l = p // 2
        c += l
        p = l * 3
    
    return c

# ---

n = int(input())
result = viralAdvertising(n)
print(result)
