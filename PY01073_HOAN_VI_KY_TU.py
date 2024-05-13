from itertools import *
s = list(input())
res = permutations(s)
for x in res:
    for i in x: print(i, end = "")
    print()
