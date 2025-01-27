#!/bin/python3

import os
import sys


#
# Complete the plusMinus function below.
#
def plusMinus(arr):
    p =0;
    n = 0;
    o = 0
    len1 = len(arr)
    for i in range(len1):
        if(arr[i] > 0):
            p+= arr[i]/len1
        elif (arr[i] < 0):
            n += arr[i] / len1
        else:
            o += arr[i] / len1
    print(p)
    print(n)
    print(o)

if __name__ == '__main__':
    arr = [-4, 3, -9, 0, 4, 1]
    plusMinus(arr)
