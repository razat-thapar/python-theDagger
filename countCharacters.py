# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 09:34:04 2018

@author: HP
"""
#returns the no of upper and lower case letters in the alphabet
#also checks whether a string is pangram or not 
import string as st
def getString():
    str=raw_input("enter the string:\n")
    return str
def evalString(s):
    l=st.ascii_lowercase
    u=st.ascii_uppercase
    L=[w for w in s]
    count_u=0
    count_l=0
    other=0
    for alpha in L:
        if(alpha in l):
            count_l+=1
        elif(alpha in u):
            count_u+=1
        else:
            other+=1
    return (count_u,count_l,other)        
def pangram(s):
    global count
    valid=False
    L=set([st.lower(w) for w in s])
    count=0
    for l in st.ascii_lowercase:
        if l in L:
           count+=1
        else:
            continue
    if (count==26):       
        valid=True
    return valid
test=getString()
(up,low,e)=evalString(test)
print "the no of uppercase: %s \tand lowercase letters are: %s \nother unicode characters are: %s \ncheck pangram :%s"%(up,low,e,pangram(test))
