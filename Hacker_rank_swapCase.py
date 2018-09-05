# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 08:10:10 2018

@author: HP
"""

#this code swaps the case of the character in the string
"""
"rAzat AggarWAl"
'RaZAT aGGARwaL'

"""
from string import *
def swap_case(s):
    str_list=[str(st) for st in s]
    for i in range(len(s)):
        if str_list[i].isupper():
            str_list[i]=lower(str_list[i])
        else:
            str_list[i]=upper(str_list[i])

    return "".join(l for l in str_list)

if __name__=='__main__':
    s=raw_input("enter any string :")
    print swap_case(s)
    