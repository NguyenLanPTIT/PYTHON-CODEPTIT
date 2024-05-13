# for _ in range (int(input())):
#     b = int(input())
#     s = input() #Xâu nhị phân đề cho ban đầu
#     x = int(s, 2) #int(n, 2) tức là chuyển xâu hệ 2 sang số hệ 10
#     if b == 2: print(s)
#     elif b==8: 
#         res = str(oct(x))
#         print(res[2::])     
#     elif b==16: 
#         res = str(hex(x))
#         res = res[2::]
#         print(res.upper())
#     elif b==4:
#         st = []
#         while(x):
#             st.append(x%4)
#             x//=4
#         for i in range (len(st) - 1, -1, -1): print(st[i], end = "")
#         print()
f = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in range(int(input())):
    n = int(input())
    s = input() #Xâu nhị phân đề cho ban đầu
    a = int(s, 2)
    res = ""
    while (a > 0):
        x = a % n
        res = f[x] + res
        a//=n
    print(res)