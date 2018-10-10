# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

#!/bin/python3

# Complete the breakingRecords function below.
def breakingRecords(scores):
    mn = mx = scores[0]
    cn = cx = 0
    for score in scores[1:]:
        if score < mn:
            mn = score
            cn += 1
        if score > mx:
            mx = score
            cx += 1
            
    return cx,cn

n = int(input())
scores = list(map(int, input().rstrip().split()))
print(' '.join(map(str, breakingRecords(scores))))
