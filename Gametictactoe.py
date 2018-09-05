# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 07:27:59 2018

@author: HP
"""

#a 2 player tic tac toe game with 3by 3 grid
#step 1 print the board as list
import string as s
import random
import time
from IPython.display import clear_output 
board=['' for i in range(0,9)]
#to clear the last output area
def output():
    clear_output() 
    print '-------------------------------------------------'
    print '|\t'+board[6]+'\t|\t'+board[7]+'\t|\t'+board[8]+'\t|'
    print '-------------------------------------------------'
    print '|\t'+board[3]+'\t|\t'+board[4]+'\t|\t'+board[5]+'\t|\t'
    print '-------------------------------------------------'
    print '|\t'+board[0]+'\t|\t'+board[1]+'\t|\t'+board[2]+'\t|'
    print '-------------------------------------------------'

def getInput():
    ch= raw_input("enter the character you want to choose 'X'or'O' \n")
    while(s.upper(ch) not in ['X','O']):
        print "invalid Character %s type again\n"%(ch)
        getInput()
    return s.upper(ch) 

def setPos(ch):
    c=ch
    try:
        temp=input("enter the position you want to put the character into eg 1,2,...8,9\n")
        pos=temp-1
    except:
        print"invalid no\n"
        setPos(input("enter the position you want to put the character into eg 0,1,2,...\n"))
    while(pos not in range(0,9) or board[pos] in ['X','O']):
        print "invalid position %s\n type again"%(pos)
        temp=input("enter the position you want to put the character into eg 0,1,2,...8\n")
        pos=temp-1
        continue
    board[pos]=c
    
        
def check(board,symbol):
    win=None
    if(board[0]==board[1]==board[2]==symbol or board[3]==board[4]==board[5]==symbol or board[6]==board[7]==board[8]==symbol ):
        win=True
    elif(board[0]==board[3]==board[6]==symbol or board[1]==board[4]==board[7]==symbol or board[2]==board[5]==board[8]==symbol ):
        win=True
    elif(board[0]==board[4]==board[8]==symbol or board[2]==board[4]==board[6]==symbol ):
        win=True
    else:
        win=False
    return win

def checkTie(board):
    tie=False
    if(check(board,'O') and check(board,'X')):
        tie=True
    elif(check(board,'O')==False and check(board,'X')==False):
        tie=True
    return tie

#program starts
def startGame():
    q=False
    starttime =time.time()
    global sp
    players={}
    p1=raw_input("enter the name of the player 1: \n")
    players[p1]=getInput()
    
    p2=raw_input("enter the name of the player 2: \n")
    #players[p2]=getInput()
    if(players[p1]=='X'):
        players[p2]='O'
    else:
        players[p2]='X'
    
    #toss for selecting the first player
    print "tossing the coin ..... \n "
    toss= random.randint(1,2)
    if toss==1:
        sp=p1
    else:
        sp=p2
    print "player to start is %s \n"%(sp)
    
    for i in range(10,0,-1):
        clear_output()
        print "The game begins at : %d"%(i)
    output()
    while(not q):
        clear_output()
        print " %s turn\n"%(sp)
        setPos(players[sp])
        output()
        if(sp == p1):
            op=p2
        else:
            op=p1
        
        if(check(board,players[sp])):
            print " %s is the winner\n"%(sp)
            break
        elif(check(board,players[op])):
            print " %s is the winner\n"%(op)
            break
        elif(checkTie(board) and len(''.join(c for c in board))==9):
            print "Its a Tie\n"
            break
        
        print " %s turn\n"%(op)
        setPos(players[op])
        output()
                
    print "game over \ntime played :%5.5f seconds\n"%(time.time()-starttime)       
    
startGame()
