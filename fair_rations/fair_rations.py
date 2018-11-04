# https://www.hackerrank.com/challenges/fair-rations/problem

#!/bin/python3

# Complete the fairRations function below.
def fairRations(B):
    # if there are odd number of odd numbers -> not possible
    o = sum(i % 2 == 1 for i in B)
    if o % 2 == 1:
        return "NO"
    
    c = 0 # counter
    i = 0
    while i < len(B)-1:
        if B[i] % 2 == 1:
            c += 2
            B[i+1] += 1
        
        i += 1
    
    return c
    
# ---

# [1,2,3] -> [2,3,3] -> [2,4,4] -> 4 (2 pairs)
# [1,1,1] -> [2,2,1] -> [2,3,2] -> [2,4,3] -> ... inf -> NO
# [2,3,4,5,6] -> [2,4,5,5,6] -> [2,4,6,6,6] -> 4 (2 pairs)
# [2,3,4,4,5] -> [2,4,5,4,5] -> [2,4,6,5,5] -> [2,4,6,6,6] -> 6 (3 pairs)
# [1,3,5,7] -> [2,4,5,7] -> [2,4,6,8] -> 4 (2 pairs)
# [1,2,3,4] -> [2,3,3,4] -> [2,4,4,4] -> 4 (2 pairs)
# [6,6,6,3,3] -> [6,6,6,4,4] -> 2 (1 pair)
# [1,4,4,1] -> [2,5,4,1] -> [2,6,5,1] -> [2,6,6,2] -> 6 (3 pairs)

    
N = int(input())
B = list(map(int, input().rstrip().split()))
result = fairRations(B)
print(result)
