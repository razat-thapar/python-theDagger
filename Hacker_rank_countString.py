# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 09:40:34 2018

@author: HP
"""
#this program counts the no of the sub string in the given string
"""
Sample Input
ABCDCDC
CDC
Sample Output
2
"""

def count_substring(string, sub_string):
    count=0
    for i in range(len(string)):
        if string[i]==sub_string[0]:
            if string[i:i+len(sub_string)]==sub_string:
                count+=1
            else:
                continue
    return count

if __name__=='__main__':
    string=raw_input("enter the string:\n")
    sub=raw_input("enter the substring:\n")
    print count_substring(string, sub)