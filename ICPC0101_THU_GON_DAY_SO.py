n = int(input())
a = list(map(int, input().split()))
# st = []  # stack lưu các số mà không ghép cặp được thành tổng chẵn
# for i in range(n):
#     if len(st)==0:  # stack rỗng --> Phần tử đang xét hiện tại không có số để ghép cặp
#         st.append(a[i])
#     else:
#         if (st[-1] + a[i]) % 2 == 0:  st.pop() # Đã có cặp
#         else: st.append(a[i])
# print(len(st))
i=0
while i < len(a) - 1:
        if (a[i] + a[i + 1]) % 2 == 0:
             del a[i]
             del a[i]
             if i > 0:
                 i -= 1
        else:
            i += 1
print(len(a))

