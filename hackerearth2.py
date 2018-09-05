# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 10:36:09 2018

@author: HP
"""

##wobby numbers
#Roy is looking for Wobbly Numbers. 
#An N-length wobbly number is of the form "ababababab..." and so on of length N, where 
#
#
#
#
#a!=b
#. 
#A 3-length wobbly number would be of form "aba". 
#Eg: 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#101,121,131,252,646
#etc
#But 
#
#
#
#
#
#
#
#
#
#
#
#111,222,999
#etc are not 3-length wobbly number, because here 
#
#
#
#
#a!=b
#condition is not satisfied.
#Also 
#
#
#
#010
#is not a 3-length wobbly number because it has preceding 0. So 
#
#
#
#010
#equals 
#
#
#10
#and 
#
#
#10
#is not a 3-length wobbly number. 
#A 4-length wobbly number would be of form "abab". 
#Eg: 
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#2323,3232,9090,1414
#etc 
#Similarly we can form a list of N-length wobbly numbers. 
#Now your task is to find K
#
#
#th
#wobbly number from a lexicographically sorted list of N-length wobbly numbers. If the number does not exist print 1 else print the Kth wobbly number. See the sample test case and explanation for more clarity. 
#Input:
#First line contains T - number of test cases 
#Each of the next T lines contains two space separated integers - N and K. 
#Output:
#For each test case print the required output in a new line. 

#variables
T=input()
N={}
K={}
wobby_no=[]
output={}

for count in range(T):
    (N[count],K[count])=(int(i) for i in raw_input().split(" "))
    
for count in range(T):
    for i in "123456789":
        for j in "0123456789":
            if(N[count]%2==0 and i!=j):
                wobby_no.append((i+j)*(N[count]/2))
            elif(N[count]%2!=0 and i!=j and N[count]!=1):
                wobby_no.append((i+j+i)*(N[count]/2))
            elif(N[count]==1):
                wobby_no.append(i)
    if(K[count] in range(1,101)):
        output[count]=wobby_no[K[count]-1]
    else:
        output[count]=-1
    wobby_no=[]

for count in range(T):
        print output[count]


