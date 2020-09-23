# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 15:07:33 2020

@author: Niranch
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    if n==1:
        return n
    else:
        return n * factorial(n-1)


n = 5

result = factorial(n)

print(result)
