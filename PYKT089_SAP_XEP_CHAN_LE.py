from sys import stdin
n = int(input())
a = []
chan = []
le = []
for line in stdin:
    x = list(map(int, line.split()))
    for i in x: a.append(i)
for i in a:
    if(i % 2 == 0):
        chan.append(i)
    else:
        le.append(i)
chan.sort(reverse= True)
le.sort()
for i in a:
    if(i % 2 == 0):
        print(chan[-1], end = " ")
        chan.pop()
    else:
        print(le[-1], end = " ")
        le.pop()