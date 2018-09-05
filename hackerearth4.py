# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 15:14:12 2018

@author: HP
"""
#positive no 
#variables

N=input()
array=[]
array=raw_input().split()
array=[int(i) for i in array]
M=input()
X=[]

for x in range(M):
    X.append(input())

def hit(x):
    for i in range(len(array)):
        if (array[i]>x):
            array[i]-=1


for x in X:
    hit(x)

#output
print " ".join([str(s) for s in array ])
