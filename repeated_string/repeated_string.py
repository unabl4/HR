# https://www.hackerrank.com/challenges/repeated-string/problem

#!/bin/python3

# Complete the repeatedString function below.
def repeatedString(s, n):
    z = n//len(s)
    c = s.count('a')
    r = s[:n%len(s)].count('a') # residue
    return z*c+r
    
# ---
    
s = input()
n = int(input())

result = repeatedString(s, n)
print(result)
