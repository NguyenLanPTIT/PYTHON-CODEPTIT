from math import *
def check(s1) :
    s2=s1[::-1]
    for i in range(0,len(s1)) :
        if abs(ord(s1[i])-ord(s1[i-1]))!=abs(ord(s2[i])-ord(s2[i-1])) : return False
    else : return True
    
for _ in range(int(input())):
    s=input()
    if check(s)==True: print("YES")
    else : print ("NO") 
    
    
    # hàm ord trả về số nguyên
    #hàm chr trả bveef kí tự (chuỗi)