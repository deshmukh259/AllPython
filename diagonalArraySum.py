#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):

    i = 0
    j = len(arr)-1
    sum1 = 0
    sum2 = 0
    for i in  range(len(arr)):
        sum1+= arr[i][i]
        sum2+=arr[j-i][i];
    sum_ = (sum1 - sum2)
    if sum_< 0:
        return sum_* -1
    else:
        return sum_



# Write your code here

if __name__ == '__main__':
    arr = [[11, 2, 4],
           [4, 5, 6],
           [10, 8, -12]]
    result = diagonalDifference(arr)
    print(result)