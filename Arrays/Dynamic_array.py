#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    arr = [[] for _ in range(n)]
    lastAnswer = 0
    answers = []
    for query in queries:
        choice = query[0]
        x = query[1]
        y = query[2] 
        if choice == 1:
            idx = ((x^lastAnswer)%n)
            arr[idx].append(y)
        else:
            idx = ((x ^ lastAnswer)%n)
            lastAnswer = arr[idx][y % len(arr[idx])]
            answers.append(lastAnswer) 
    return answers

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

"""
Space Complexity:
    - O(n+q) where n is the size of the sequence and q is the number of queries.
Time Complexity:
    - O(p) where p is the size of the sequence.
"""