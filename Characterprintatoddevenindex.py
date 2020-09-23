# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 09:25:52 2020

@author: Niranch
"""

#Print even and odd indexed string with a space for a given input string that ranges from 1 to 10 strings

inputlist=[]
while True:
    data = input("Please enter count to strings to process followed by strings in each line(Enter Exit to break):\n")
    if 'Exit' == data:
        break
    else:
        inputlist.append(data)
        
       
[print(i) for i in inputlist]

if int(inputlist[0]) <=10 and int(inputlist[0])>=1:
    inputlist.pop(0)
    for i in inputlist:
        print(i)
        los=len(i)
        print(los)
        if los>=2 and los<=10000:
            print(i[0:los:2]+" "+i[1:los:2])
            