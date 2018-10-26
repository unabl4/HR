# https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

#!/bin/python3

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    n = len(c)
    def g(i,j):
        # i - current index (cloud)
        # j - number of jumps
        
        # recursion base case
        if i == n-1: # end cloud?
            return j # return the number of jumps so far
        
        r = [i+1,i+2] # range
        return min(g(v,j+1) for v in r if v < n and not c[v])    
    
    return g(0,0)
    
    
# ---

n = int(input())
c = list(map(int, input().rstrip().split()))

result = jumpingOnClouds(c)
print(result) # min number of jumps
