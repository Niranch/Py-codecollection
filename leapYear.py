# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 20:47:51 2020

@author: Niranch
"""

#leap year problem

def is_leap(year):
    leap = False
    
    # Write your logic here
    if year % 4 == 0:
        leap = True
        if year % 100 == 0:
            leap = False
            if year % 400 == 0:
                leap = True
       
    
    return leap

year = int(raw_input())