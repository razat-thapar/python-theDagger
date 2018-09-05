# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 13:40:44 2018

@author: HP
"""

#matrix

#variables
row_matrix=[]
col_matrix=[]
total1=False
total2=False
path1=[]
path2=[] 
N=input()

#logic

for r in range(N):
    row_matrix.append([int(d) for d in raw_input().split(' ')])

#transpose of row_matrix
temp=[]
for i in range(N):
    for j in range(N):
        temp.append(row_matrix[j][i])
    col_matrix.append(temp)


def charIn(row,c):
    if(c in row):
        return True
    else:
        return False
        
def check1Path():        
    for r in row_matrix:
        if(charIn(r,1)):
            path1.append(1)   
        else:
            path1.append(0)
    pro1=0
    for i in range(N):
        pro1=pro1*path1[i] 
    if(pro1==1):
        return True
    else:
        return False
#check path of 2's
def check2Path():
    for r in col_matrix:
        if(charIn(r,2)):
            path2.append(1)   
        else:
            path2.append(0)
    pro2=1
    for i in range(N):
        pro2=pro2*path2[i]

    if(pro2==1):
        return True
    else:
        return False

#output
if()
    if(check1Path()):
        if(check2Path()):
            print "AMBIGUOUS"
        else:
            print '1'
    else:
        if(check2Path()):
            print '2'
        else:
            print '0'
    