from functools import cmp_to_key
def tich(n):
    res = 1
    for x in str(n): res*=int(x)
    return res
def cmp(a, b):
    if tich(a) != tich (b): return tich(a) - tich(b)
    elif a != b: return a - b
for _ in range (int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(key = cmp_to_key(cmp))
    for x in a: print(x, end = " ")
    print()
