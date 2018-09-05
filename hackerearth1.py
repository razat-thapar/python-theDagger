# -*- coding: utf-8 -*-
"""
Created on Sun Apr 15 03:35:50 2018

@author: HP
"""

import random
#variables
weight={}

sum_weight=0
input_string=[]

s_string={}
weight_sub_string={}
count_sub_string={}
sub_string=set()
sub_strings={}

count_strings=input()
loop=0
while(loop<count_strings):
    weight_sub_string[loop]=input()
    s_string[loop]=raw_input()
    loop+=1

#assign weights to char
i=1
for char in "abcdefghijklmnopqrstuvwxyz":
    weight[char]=i
    i+=1
v=True
for test_cases in range(0,count_strings):
    w=weight_sub_string[test_cases]
    s=s_string[test_cases]
    count=100
    while(count>0):
        n=random.randint(1,w+1)
        st=random.sample(s,n)
        total_weight=sum([weight[ch] for ch in st])
        if (total_weight== w):
            sub_string.add("".join(st))
        count=count-1
    count_sub_string[test_cases]=len(sub_string)
    sub_strings[test_cases]=sub_string
    sub_string.clear()

for c in count_sub_string.values():
    print c 