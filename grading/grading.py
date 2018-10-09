# https://www.hackerrank.com/challenges/grading/problem

#!/bin/python3

import os
import sys
from math import ceil

#
# Complete the gradingStudents function below.
#
def gradingStudents(grades):
    rounded_grades = []
    for grade in grades:
        new_grade = grade
        if grade >= 38:
            next_mult = ceil(grade / 5) * 5
            if next_mult-grade < 3:
                new_grade = next_mult
        rounded_grades.append(new_grade)
    return rounded_grades

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
