# https://www.hackerrank.com/challenges/counting-valleys/problem

#!/bin/python3

# Complete the countingValleys function below.
def countingValleys(steps):
    l = 0
    d = { 'U': 1, 'D': -1 }
    c = 0
    for step in steps:
        nl = l+d[step]           
        if nl >= 0 and l < 0:
            c += 1
        
        l = nl
    return c

# ---

n = int(input())
s = input()

result = countingValleys(s)
print(result)
