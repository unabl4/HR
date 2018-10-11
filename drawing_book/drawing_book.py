# https://www.hackerrank.com/challenges/drawing-book/problem

#!/bin/python3

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    if n % 2 == 0:
        n += 1
    return min(p//2, (n-p)//2)

# [0,1],[2,3],[4,5],[6,7]
n = int(input())
p = int(input())
result = pageCount(n, p)
print(result)
