#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countApplesAndOranges' function below.
#
# The function accepts following parameters:
#  1. INTEGER s
#  2. INTEGER t
#  3. INTEGER a
#  4. INTEGER b
#  5. INTEGER_ARRAY apples
#  6. INTEGER_ARRAY oranges
#

def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Calculating distance for apple
    for i in range(len(apples)):
        apples[i] = apples[i] + a

    # Calculating distance for oranges
    for i in range(len(oranges)):
        oranges[i] = oranges[i] + b

    # Apples in range
    count_apple = 0
    for value in apples:
        if s <= value <= t:
            count_apple += 1

    # Oranges in range
    count_orange = 0
    for value in oranges:
        if s <= value <= t:
            count_orange += 1

    print(f"{count_apple}\n{count_orange}")



if __name__ == '__main__':

    while True:
        first_multiple_input = input().rstrip().split()

        s = int(first_multiple_input[0])

        t = int(first_multiple_input[1])

        if s < t:
            break

    while True:
        second_multiple_input = input().rstrip().split()

        a = int(second_multiple_input[0])

        b = int(second_multiple_input[1])

        if a < s < t < b:
            break

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    # apples distance from tree
    apples = list(map(int, input().rstrip().split()))
    # oranges distance from tree
    oranges = list(map(int, input().rstrip().split()))



    countApplesAndOranges(s, t, a, b, apples, oranges)
