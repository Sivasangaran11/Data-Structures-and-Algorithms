#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING expression as parameter.
#

def isBalanced(expression):
    stack = []
    openBrackets = ['{','(','[']
    for bracket in expression :
        if bracket in openBrackets:
            stack.append(bracket)
            print(stack)
        else:
            if not stack:
                return "NO"
            topBracket = stack.pop()
            if topBracket == '[' and bracket == ']':
                continue
            if topBracket == '(' and bracket == ')':
                continue
            if topBracket == '{' and bracket == '}':
                continue
            return "NO"
        print(stack)
    if not stack:
        return 'YES'
    return "NO"
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        expression = input()

        res = isBalanced(expression)

        fptr.write(res + '\n')

    fptr.close()