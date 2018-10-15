# https://www.hackerrank.com/challenges/angry-professor/problem

#!/bin/python3

# Complete the angryProfessor function below.
def angryProfessor(k, a):
    return "NO" if sum([x <= 0 for x in a]) >= k else "YES"

t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    a = list(map(int, input().rstrip().split()))
    result = angryProfessor(k, a)
    print(result)
