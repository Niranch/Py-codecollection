# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 20:28:43 2020

@author: Niranch
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT


import sys
inputlist=[]
mydict={}
for line in sys.stdin:
    if 'Exit' == line.rstrip():
        break
    else:
        inputlist.append(line.rstrip())
if(len(inputlist)>=1):        
    itemsCnt=int(inputlist[0])
    inputlist.pop(0)
    j=1
    #Creating and Adding values to the dictionary Object
    if itemsCnt>=1 and itemsCnt<=100000:
        if len(inputlist)<=100000 and len(inputlist)>=1:
            for i in inputlist:
                if(j<=itemsCnt):
                    s=i.split(" ")
                    mydict[s[0]]=s[1]
                    j+=1
    
    #Getting values from dictionary Object for given input
    checklist = inputlist[itemsCnt:]
    for i in checklist:
        if i in mydict:
            print(i+"="+mydict[i])
        else:
            print("Not found")