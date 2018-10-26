# https://www.hackerrank.com/challenges/taum-and-bday/problem

#!/bin/python3

# Complete the taumBday function below.
def taumBday(b, w, bc, wc, z):
    x = min(bc, wc+z) * b
    y = min(wc, bc+z) * w
    return x+y
    
# ---

t = int(input())
for _ in range(t):
    b,w = map(int, input().split())
    bc,wc,z = map(int, input().split())
    result = taumBday(b, w, bc, wc, z)
    print(result)
