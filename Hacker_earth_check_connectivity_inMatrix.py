'''
Now given a matrix of 0, 1 or 2, do your computation according to the following rules:
	If there is a path from any position in top row to any position in bottom row consisting only of 1, then print 1.
	If there is a path from any position in first column to any position in last column consisting only of 2, then print 2.
	If both Rule 1 & Rule 2 are true, print'AMBIGUOUS' .
	If none of Rule 1, Rule 2 or Rule 3 satisfies, print 0.
Input format
First line of input contains a positive integer N, the size of matrix. Then N line follows, each containing N integers which are either 0, 1 or 2.
'''
#code:
size=int(raw_input())
matrix=[]
for i in range(size):
    matrix.append([int(s) for s in raw_input().split(' ')])

def check_row(lst):
    position=[]
    for j in range(len(lst)) :
        if(lst[0][j]==1):
            position.append(j)
    for pos in position:
        for row in range(1,len(lst)):
            if(lst[row][pos-1]==1 or lst[row][pos]==1 or lst[row][pos+1]==1):
                continue
            else:
                return False
        return True
def check_col(lst):
    position=[]
    for j in range(len(lst)) :
        if(lst[j][0]==2):
            position.append(j)
    for pos in position:
        for col in range(1,len(lst)):
            if(lst[pos-1][col]==2 or lst[pos][col]==2 or lst[pos+1][col]==2):
                continue
            else:
                return False
        return True

if(size in range(101)):
    check1=check_row(matrix)
    check2=check_col(matrix)
    if(check1):
        if(check2):
            print "AMBIGUOUS"
        else:
            print 1
    elif(check2):
        print 2
    else:
        print 0
    