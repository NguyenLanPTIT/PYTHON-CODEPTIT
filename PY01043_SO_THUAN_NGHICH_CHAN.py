# from collections import deque
# s = "02468"
# v = ["22", "44", "66", "88"] #vector lưu các xâu thuận nghịch độ dài chẵn

# #Idea: Sinh ra các số chứa 0, 2, 4, 6, 8 đến 3 chữ số rồi đảo ngược lại
# def gen():
#     #Bước 1: Khởi tạo
#     q = deque()
#     for i in range (1, len(s)): q.append(s[i]) #Các số 0, 2, 4, 6, 8 là các cấu hình cơ sở đưa vào qe 
#     #Bước 2: Lặp:
#     while True:
#         x = q.popleft() #Lưu đỉnh hàng đợi và xóa đi 
#         if len(x)==3: break
#         #Từ đỉnh hàng đợi loang ra các cấu hình khác
#         for i in s: 
#             s1 = x + i
#             s2 = s1[::-1] #Tạo xâu đảo ngược
#             q.append(s1)
#             v.append(s1 + s2)

# gen()
# for k in range (int(input())):
#     n = int(input())
#     for i in v:
#         if int(i) < n: print(i, end = " ")
#         else: break
#     print()
def check(s):
    if len(s)%2==1 or s!= s[::-1]: return False
    for x in s: 
        if int(x)%2==1: return False
    return True

for _ in range(int (input())):
    n=int (input())
    for i in range (2,n):
        if check(str(i)): print (i,end=" ")
    print ()   