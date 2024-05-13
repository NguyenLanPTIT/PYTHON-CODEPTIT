from math import*
def check(s):
    for i in s :
        if int (i)%2==1: return False
    if len(s)%2==1 or s!=s[::-1]: return False
    return True
for _ in range(int (input())):
    n=int (input())
    for i in range (2,n,2):
        if check(str(i)): print (i,end=" ")
    print ()   