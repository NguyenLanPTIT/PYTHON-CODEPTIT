from math import *
for _ in range(int(input())):
    s= input()
    sum=1
    for i in range(1,len(s)):
        if s[i]!=s[i-1] :
            print (sum,end="")
            print (s[i-1],end="")
            sum=1
        else : sum+=1
    print (sum,end="")
    print (s[len(s)-1])