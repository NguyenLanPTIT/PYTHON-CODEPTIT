for i in range(int(input())) :
    ok = 0
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()
    for i in range(n) :
        if a[i] > b[i] :
            ok = 1
            break
    if ok == 0 : print("YES")
    else : print("NO")