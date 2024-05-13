prime = [1] * 1000001
def sang():
    prime[0] = prime[1] = 0 #vị trí 0, 1 không phải nguyên tố , đánh dấu là 0
    for i in range (2, 1001): #trong đề n chạy đến 10^6 nên đây chỉ cần chạy đến căn(10^6)=1001-1
        if prime[i]: #nếu vị trí i là nguyên tố (=1)
            for j in range (i*i, 1000001, i): prime[j] = 0 #đánh dấu bội của i không phải nguyên tố (=0)
sang()
for _ in range(int(input())):
    n = int(input())
    for i in range (13, n):
        rev = int(str(i)[::-1])
        #Trong mỗi cặp số bắt buộc i nhỏ hơn rev, in i trước rev sau
        if prime[i] and prime[rev] and rev > i and rev < n : print(i, rev, sep = " ", end =" ")
    print()