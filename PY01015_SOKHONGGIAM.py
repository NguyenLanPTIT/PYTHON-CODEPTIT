from math import *
def khonggiam ( s) :
    for i in range(len(s)-1) :
        if ( s[i]> s[i+1]) : return False
    return True


for _ in range(int(input())) :
    s= input()
    if (khonggiam(s)): print("YES")
    else : print ("NO")