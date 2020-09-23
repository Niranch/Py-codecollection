# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:17:38 2020

@author: Niranch
"""

import math
import os
import random
import re
import sys

listofSum=[]
#arr = [[random.choice(range(-9,9) for i in range(6)] random.choice(range(-9,9) for j in range(6)] 
arr=[[0,2,3,1,8,6],[4,3,2,7,1,3],[8,6,3,5,2,1],[9,6,7,8,3,1],[0,3,2,1,3,1],[3,2,4,0,-2,-1]]
for i in range(0,4):
    #Getting three elements from each col in the ith row
    for j in range(0,4):
        total=(arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
        listofSum.append(total)
        print(total)

print("Max",max(listofSum))