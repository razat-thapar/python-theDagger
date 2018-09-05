# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 10:40:45 2018

@author: HP
"""

#using oop concepts to find the slope and the length of a line segment given two points
class Line(object):
    def __init__(self,cor1,cor2):
        self.cor1=cor1
        self.cor2=cor2
    def slope(self):
        if(self.cor2[0]-self.cor1[0] !=0):
            return (self.cor2[1]-self.cor1[1])/(self.cor2[0]-self.cor1[0])
        else:
            return "infinte slope\n"
    def leng(self):
        l=(self.cor2[0]-self.cor1[0])**2 + (self.cor2[1]-self.cor1[1])**2
        return l**0.5


#creating an instance of class
l=Line((1,2),(3,4))
print "slope :%.5f \nlength :%.5f"%(l.slope(),l.leng())

