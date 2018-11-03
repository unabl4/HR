# https://www.hackerrank.com/challenges/halloween-sale/problem

#!/bin/python3

# Complete the howManyGames function below.
def howManyGames(p,d,m,s):
    # Return the number of games you can buy        
    # check to see if 'S' can be fulfilled solely by means of the elements of the progression
    a = -d
    b = 2*p+d
    c = -2*s
    D = b*b - 4*a*c # discriminant
    
    if D >= 0:
        # solution exists -> solve for 'n' and return the number
        z = (D**0.5-b) // (2*a)
    else:
        # there are definitely more to it
        
        # An=A1+(n-1)d
        # An-A1=(n-1)d
        # (n-1)=(An-A1)/d
        # n = (An-A1)/d+1
        z = 0
        n = (p-m)//d+1 # number of elements in the progression (floor)
        # end check
        z += n
        an = p+(n-1)*(-d) # end value
        ps = (p+an)*n/2 # progression sum
        z += max(s-ps,0) // m   # the rest is at const price
    return int(z)

# ---

p,d,m,s = map(int, input().split())
answer = howManyGames(p,d,m,s)
print(answer)
