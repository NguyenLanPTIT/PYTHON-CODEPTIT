# for _ in range(int(input())):
#     n = int(input())
#     d = dict()
#     for i in range(n):
#         x = int(input())
#         if x in d: d[x] += 1 
#         else: d[x] = 1 
#     res = list(d.items())
#     res.sort(key = lambda x: (-x[1], x[0]))
#     print(res[0][0])

if __name__ == "__main__":
  t = int(input())
  while t > 0:
    t -= 1
    n = int(input())
    cnt = [0] * 1001
    Max, value = 0, 0
    for i in range(n):
      x = int(input())
      cnt[x] += 1
      if cnt[x] > Max:
        Max = cnt[x]
        value = x
      elif cnt[x] == Max:
        if x < value:
          value = x
    print(value)