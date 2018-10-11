# https://www.hackerrank.com/challenges/picking-numbers/problem

#!/bin/python3

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    b = sorted(a)
    x = 0 
    y = 1
    c = 0 # max counter
    
    while True:
        if y >= len(a):
            break
            
        if abs(b[y]-b[x]) > 1:
            x = y
            
        c = max(c,y-x+1) # update max
        y+=1 # move forward
    
    return c

# ---

n = int(input().strip())
a = list(map(int, input().rstrip().split()))

result = pickingNumbers(a)
print(result)
