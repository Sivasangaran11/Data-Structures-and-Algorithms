#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

def equalStacks(h1, h2, h3):
    sum1, sum2, sum3 = map(sum, (h1, h2, h3))
    height1, height2, height3 = 0, 0, 0
    
    while True:
        if height1 >= len(h1) or height2 >= len(h2) or height3 >= len(h3):
            return 0
        
        if sum1 == sum2 == sum3:
            return sum1
        
        if sum1 >= sum2 and sum1 >= sum3:
            sum1 -= h1[height1]
            height1 += 1
        elif sum2 >= sum1 and sum2 >= sum3:
            sum2 -= h2[height2]
            height2 += 1
        elif sum3 >= sum1 and sum3 >= sum2:
            sum3 -= h3[height3]
            height3 += 1
    return 0 


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()