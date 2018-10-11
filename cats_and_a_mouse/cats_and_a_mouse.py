# https://www.hackerrank.com/challenges/cats-and-a-mouse/problem

#!/bin/python3

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    d1 = abs(x-z)
    d2 = abs(y-z)
    
    if d1 == d2:
        return "Mouse C"
    elif d1 < d2:
        return "Cat A"
    else:
        return "Cat B"
    
# ---
    
q = int(input())
for q_itr in range(q):
    x,y,z = map(int, input().split())
    result = catAndMouse(x, y, z)
    print(result)
