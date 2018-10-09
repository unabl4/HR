# https://www.hackerrank.com/challenges/kangaroo/problem

#!/bin/python3

import math
import os
import random
import re
import sys

# x1+t*v1=x2+t*v2
# x1+t*v1-x2-t*v2=0
# x1-x2+tv1-tv2=0
# x1-x2+t(v1-v2)=0
# t(v1-v2)=x2-x1
# t = (x2-x1)/(v1-v2)

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    vd = v1-v2
    xd = x2-x1   # x2 > x1 by definition => pos
    return "YES" if vd > 0 and xd % vd == 0 else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
