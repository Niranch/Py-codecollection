# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 19:31:59 2020

@author: Niranch
"""

from array import *
n=5
mylist=[6,6,6,6,6]
mylist.sort()
flag=False
while n>0:
    
    if mylist[n-2]!=mylist[n-1]:
       runnerup = mylist[n-2]
       flag=True
    else:
        n=n-1
    if(flag) or (n<0):
        break
if(flag):
    print(runnerup)
else:   
    print("All are winners")