# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 20:07:44 2020

@author: Niranch
"""


x= range(3)
y=range(5)
z=range(8)



print([[i,j,k] for i in x for j in y for k in z if i+j+k>2])

#==============================================================================
# 
# print([[x, y] for x in [1, 2, 3] for y in [4, 5, 6]])
# [[1, 4], [1, 5], [1, 6], [2, 4], [2, 5], [2, 6], [3, 4], [3, 5], [3, 6]]
#==============================================================================
