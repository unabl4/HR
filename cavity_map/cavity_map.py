# https://www.hackerrank.com/challenges/cavity-map/problem

#!/bin/python3

# Complete the cavityMap function below.
def cavityMap(grid):
    h = len(grid)
    w = len(grid[0])
    d = [(-1,0),(0,1),(1,0),(0,-1)] # top, right, bottom, left
    z = set() # change set
    for y in range(1,h-1):
        for x in range(1,w-1):
            c = True # is cavity?
            # check neightbour cells
            for dx,dy in d:
                if grid[y+dy][x+dx] >= grid[y][x]:
                    c = False
                    break
            
            if c:
                z.add((y,x))
                
    # mark
    for y,x in z:
        r = list(grid[y])
        r[x] = 'X'
        grid[y] = ''.join(r)
    return grid

# ---
    
n = int(input())
grid = []
for _ in range(n):
    grid_item = input()
    grid.append(grid_item)

result = cavityMap(grid)
print('\n'.join(result))
