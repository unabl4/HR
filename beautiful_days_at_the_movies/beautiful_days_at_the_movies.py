# https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem

#!/bin/python3

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    return sum(abs(x-int(str(x)[::-1]))%k==0 for x in range(i,j+1))

i,j,k = map(int, input().split())
result = beautifulDays(i, j, k)
print(result)
