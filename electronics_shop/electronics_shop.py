# https://www.hackerrank.com/challenges/electronics-shop/problem

#!/bin/python3

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    found = False
    closest = b
    for k in keyboards:
        for d in drives:
            diff = b-k-d
            if diff >= 0 and diff < closest:
                found = True
                closest = diff
                
    return b-closest if found else -1

# ---

b,n,m = map(int, input().split())
keyboards = list(map(int, input().rstrip().split()))
drives = list(map(int, input().rstrip().split()))

moneySpent = getMoneySpent(keyboards, drives, b)
print(moneySpent)
