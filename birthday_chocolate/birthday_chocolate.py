# https://www.hackerrank.com/challenges/the-birthday-bar/problem

#!/bin/python3

# Complete the birthday function below.
def birthday(s, d, m):
    w = sum(s[:m])
    i = 0
    j = m-1
    c = 0 # counter
    while True:
        if w == d:
            c += 1
        
        if j+1 >= len(s):
            break
        
        w = w-s[i]+s[j+1]
        i+=1
        j+=1
        
    return c

n = int(input().strip())
s = list(map(int, input().rstrip().split()))
dm = input().rstrip().split()

d = int(dm[0])
m = int(dm[1])

result = birthday(s, d, m)
print(result)
