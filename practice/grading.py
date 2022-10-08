#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    rounding = []
    for value in grades:
        if value < 38:
            rounding.append(value)
        else:
            find_next = ((value/5.0)+1) // 1
            find_next = find_next * 5
            diff = find_next - value
            if diff < 3:
                rounding.append(find_next)
            else:
                rounding.append(value)
    return rounding


if __name__ == '__main__':
    '''fptr = open(os.environ['OUTPUT_PATH'], 'w')
    while True:
        grades_count = int(input().strip())
        if 1 <= grades_count <= 60:
            break'''

    grades = [73, 67, 38, 33]

    '''for _ in range(grades_count):
        grades_item = int(input().strip())
        while True:
            if 0 <= grades_item <= 100:
                grades.append(grades_item)
                break
            else:
                grades_item = int(input().strip())'''
    result = gradingStudents(grades)
    print(result)
