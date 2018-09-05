# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 09:16:35 2018

@author: HP
"""

#matrix
#inputs
#2
#3 3
#1 2
#output
#30 
#2

#variables
T=input()
M={}
A={}
B={}
r=0
c=0
Trace=[]

def buildA(l):
    (r,c)=(i for i in l)
    count_r=1
    row=[]
    matrix=[]
    for i in range(r):
        for col in range(c):
            row.append(count_r)
            count_r+=1
        matrix.append(row)
        row=[]
    return matrix    
    
def buildB(l):
    (r,c)=(i for i in l)
    count_c=1
    col=[]
    matrix=[]
    for co in range(c):
        for row in range(r):
            col.append(count_c)
            count_c+=1
        matrix.append(col)
        col=[]
    return matrix

for t in range(T):
    M[t]=[int(i) for i in raw_input().split()]
    A[t]=buildA(M[t])
    B[t]=buildB(M[t])




for t in range(T):
    trace=0
    for i in range(min(M[t])):
        trace=trace+A[t][i][i]+B[t][i][i]
    Trace.append(trace)

#output
for t in Trace:
    print t
