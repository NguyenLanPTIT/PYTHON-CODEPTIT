f='0123456789ABCDEF'
file = open('DATA.in', 'r')
for _ in range (int(file.readline())):
    n = int(file.readline())
    s = file.readline()
    a=int(s,2)
    res=""
    while (a>0):
        x=a%n
        res=f[x]+res
        a//=n
    print(res)