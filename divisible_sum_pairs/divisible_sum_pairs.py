# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

#!/bin/python3

# Complete the divisibleSumPairs function below.
# naive implementation -> most definitely not going to pass
def divisibleSumPairs(n, k, ar):
    c = 0
    for i in range(n):
        for j in range(i+1,n):
            if (ar[i]+ar[j]) % k == 0:
                c += 1
    return c

# ---

n, k = map(int, input().split())
ar = list(map(int, input().rstrip().split()))

result = divisibleSumPairs(n, k, ar)
print(result)
