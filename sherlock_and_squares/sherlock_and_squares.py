# https://www.hackerrank.com/challenges/sherlock-and-squares/problem

#!/bin/python3

# Complete the squares function below.
def squares(a,b):
    x = -int(-a**0.5//1)
    y = int(b**0.5//1)
    return y-x+1
        
q = int(input())
for _ in range(q):
    a,b = map(int, input().split())
    result = squares(a,b)
    print(result)
