from math import *
prime =[1]*10001
def sang():
    prime[0]=prime[1]=0
    for i in range(2,int(sqrt(10001))):
        if prime[i]:
            for j in range(i*i,10001,i): prime[j]=0
sang()
for _ in range (int(input())):
    n=int(input())
    res=0
    for i in range(1,n):
        if gcd(i,n)==1: res+=1
    if prime[res]==1: print("YES")
    else: print("NO")   
