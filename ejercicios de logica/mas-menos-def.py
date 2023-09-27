#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    #print(arr)
    a = len(arr)    
    neg = 0
    posi = 0
    cero = 0

    for x in arr:
        if x < 0:
            neg = 1 + neg
        elif x > 0:
            posi = 1 + posi
        elif x == 0:
            cero = 1 + cero
        #print(neg)    
        # print(posi)    
        # print(cero)    
    
    
        
        
        m = neg / a
        l = posi / a    
        c = cero / a      
    
    print("{0:.6f}".format(l))
    print("{0:.6f}".format(m))
    print("{0:.6f}".format(c))
    


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)