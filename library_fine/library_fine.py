# https://www.hackerrank.com/challenges/library-fine/problem

#!/bin/python3

# Complete the libraryFine function below.
def libraryFine(d1, m1, y1, d2, m2, y2):
    df = 15 # day fine (same calendar month)
    mf = 500 # month fine (same calendar year)
    yf = 10000 # calendar year fine
 
    if y1 < y2:
        return 0
    elif y1 == y2:
        # at least same calendar year
        if m1 == m2:
            # at least the same calendar month
            if d1 > d2:
                return (d1-d2) * df
        elif m1 > m2:
            # not the same month
            return (m1-m2) * mf
    else: # >
        return yf # fixed value

    return 0
    
# ---
    
d1,m1,y1 = map(int, input().split()) # return date
d2,m2,y2 = map(int, input().split()) # due date
result = libraryFine(d1, m1, y1, d2, m2, y2)
print(result)
