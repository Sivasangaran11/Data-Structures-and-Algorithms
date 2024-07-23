#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

def getMax(operations):
    stack = []
    max_stack = []
    res = []
    
    for operation in operations:
        parts = operation.split()
        if parts[0] == "1":
            value = int(parts[1])
            stack.append(value)
            if not max_stack or value >= max_stack[-1]:
                max_stack.append(value)
        elif parts[0] == "2":
            if stack:
                popped_value = stack.pop()
                if popped_value == max_stack[-1]:
                    max_stack.pop()
        elif parts[0] == "3":
            if max_stack:
                res.append(max_stack[-1])
    
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
