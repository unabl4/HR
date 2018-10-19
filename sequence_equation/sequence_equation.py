# https://www.hackerrank.com/challenges/permutation-equation/problem

#!/bin/python3

# Complete the permutationEquation function below.
def permutationEquation(p):
    m = {}
    for a,b in enumerate(p):
        m[b] = a+1
        
    return [m[m[x+1]] for x in range(len(p))]

n = int(input())
p = list(map(int, input().rstrip().split()))
result = permutationEquation(p)
print('\n'.join(map(str, result)))
