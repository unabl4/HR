# https://www.hackerrank.com/challenges/bon-appetit/problem

#!/bin/python3

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    amt = (sum(bill)-bill[k]) / 2
    return "Bon Appetit" if amt == b else int(b-amt)
    
if __name__ == '__main__':
    n,k = map(int, input().rstrip().split())
    bill = list(map(int, input().rstrip().split()))
    b = int(input().strip())
    
    print(bonAppetit(bill, k, b))
