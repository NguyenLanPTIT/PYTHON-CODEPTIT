t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    d = [0] * n
    st = []
    for i in range(n):
        while st and a[i] >= a[st[-1]]: # khi nào a[i] còn lớn hơn các ptu có chỉ số trong st (lớn hơn các ptu ở trước a[i] trong ds a)
            st.pop() # xóa chỉ số của các ptu nhỏ hơn a[i] ra khỏi st
        if not st: # nếu st rỗng
            d[i] = i + 1 # các chỉ só của ptu nhỏ hơn a[i] đề đã bị xóa ra khỏi st 
        else: # nếu st k rỗng
            d[i] = i - st[-1] # số lượng ptu nhỏ hơn hoặc bằng a[i] chính là khoảng từ chỉ số i đến ptu cuối cùng trong st
        st.append(i)
    print(*d)