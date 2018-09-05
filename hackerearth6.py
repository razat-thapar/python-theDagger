# -*- coding: utf-8 -*-
"""
Created on Tue Apr 17 16:19:35 2018

@author: HP
"""
#previous date

#variables
month_list={'January':31,'February':28,'March':31,'April':30,'May':31,'June':30,'July':31,'August':30,'September':30,'October':31,'November':30,'December':31}
previous_month={'January':'December','February':'January','March':'February','April':'March','May':'April','June':'May','July':'June','August':"July",'September':"August",'October':"September",'November':"October",'December':'November'}
month_list_l={'January':31,'February':29,'March':31,'April':30,'May':31,'June':30,'July':31,'August':30,'September':30,'October':31,'November':30,'December':31}

T=input()
date=[]
for t in range(T):
    date.append(raw_input().split())
previous_date=[]

def check_leapyear(y):
    if(y%400==0):
        return True
    elif(y%100==0):
        return False
    elif(y%4==0):
        return True
    else:
        return False
            
#program
if(T<=100):
    for d in date:
        day=int(d[0])
        month=d[1]
        year=int(d[2])
        if(day>1):
            previous_date.append([day-1,month,year])
        elif(month=="March" and day==31):
            if(check_leapyear(year)):
                previous_date.append([29,"February",year])
            else:
                previous_date.append([28,"February",year])
        elif(day==1 and month!='January'):
            if(check_leapyear(year)):
                previous_date.append([month_list_l[previous_month[month]],previous_month[month],year])
            else:
                previous_date.append([month_list[previous_month[month]]+1,previous_month[month],year])
        elif(day==1 and month=='January'):
                previous_date.append([month_list[previous_month[month]],previous_month[month],year-1])
            
for i in previous_date:
    print i