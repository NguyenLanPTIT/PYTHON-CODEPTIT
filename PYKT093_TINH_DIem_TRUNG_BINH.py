def chuanhoa(s):
    a = s.strip().split()
    res = ""
    for x in a: res += x.capitalize() + " "
    return res

from math import *
class SinhVien:
    def __init__(self, x, name, x1, x2, x3):
        self.id = "SV" + "{:02d}".format(x)
        self.name = chuanhoa(name)
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.tbc = ceil((self.x1 * 3 + self.x2 * 3 + self.x3 * 2) / 8.0 * 100) / 100
    
    def __str__(self):
        return f"{self.id} {self.name} {self.tbc:.2f} {self.xepHang}"

if __name__ == "__main__":
    n = int(input())
    a = []
    for i in range(n):
        a.append(SinhVien(i + 1, input(), float(input()), float(input()), float(input())))
    a.sort(key = lambda x: (-x.tbc, x.id))
    a[0].xepHang = 1
    for i in range(1, len(a)):
        if a[i].tbc == a[i - 1].tbc:
            a[i].xepHang = a[i - 1].xepHang
        else:
            a[i].xepHang = i + 1
    print(*a, sep = '\n')