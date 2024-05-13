# from sys import stdin 
# res = set()
# for line in stdin:
#     a = list(map(int, line.split()))
#     for i in a: res.add(i%42)
# print(len(res))
# #stdin đọc  nhiều đầu vào và tự động thêm \n sau mỗi câu
from math import *
se=set()
while True:
    try:
        s= map(int,input().split())
        for i in s:
            se.add(i%42)
    except :
        break;    
print(se)