# https://www.hackerrank.com/challenges/migratory-birds/problem

#!/bin/python3

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    f = {}
    for bird in arr:
        f[bird] = f.get(bird,0)+1
        
    return max(range(1,6), key=lambda k: f.get(k,0))
    
# ---

arr_count = int(input().strip())
arr = list(map(int, input().rstrip().split()))

result = migratoryBirds(arr)
print(result)
