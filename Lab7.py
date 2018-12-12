##CS 2302 Data Structures
##Instructor:Diego Aguirre
##TA: Anindita Nath
##Project 7 Option A
##Modified and submitted by Andres Ponce 80518680
##Date of last modification 12/11/2018
##Purpose: Implement the dynamic-programming algorithm
##Edit Distance

import os
import random
import time
import re
import math

####   Edit Distance   ####
def edit_distance(string1, string2, sizeStr1, sizeStr2):
    
    #Base cases
    if string1==string2:
        return
    
    if sizeStr1==0:
        return sizeStr2

    if sizeStr2==0:
        return sizeStr1

    #Recursive call when the last characters are same
    if string1[sizeStr1-1] == string2[sizeStr2-1]:
        return edit_distance(string1, string2, sizeStr1-1, sizeStr2-1)
    
    #Recursive counter to compute the minimum value of operations: insert, remove,
    #and replace when the last character is not the same.
    return 1 + min(edit_distance(string1, string2, sizeStr1, sizeStr2-1),
                   edit_distance(string1, string2, sizeStr1-1, sizeStr2),
                   edit_distance(string1, string2, sizeStr1-1, sizeStr2-1))


