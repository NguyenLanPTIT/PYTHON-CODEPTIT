# def custom_round(number, decimal_places):
#     factor = 10 ** decimal_places
#     rounded_number = int(number * factor + 0.5) / factor
#     return rounded_number
from decimal import *
class HSinh:
    count=0
    def __init__(self, name, diem):
        HSinh.count+=1
        self.id = f'HS{HSinh.count:02d}'
        self.name = name
        a=[float(i) for i in diem.split()]
        self.tbc=(((a[0] + a[1]) * 2.0 + sum(a[2:])) / 12.0)
        self.tbc= round(self.tbc+0.01,1)
        if self.tbc >= 9.0:
            self.xeploai = "XUAT SAC"
        elif self.tbc >= 8.0:
            self.xeploai = "GIOI"
        elif self.tbc >= 7.0:
            self.xeploai = "KHA"
        elif self.tbc >= 5.0:
            self.xeploai = "TB"
        else:
            self.xeploai = "YEU"

    def __str__(self):
        return f"{self.id} {self.name} {self.tbc:.1f} {self.xeploai}"

if __name__ == "__main__":
    a = []
    for i in range(int(input())):
        a.append(HSinh(input(),input()))

    a.sort(key=lambda x: (-x.tbc, x.id))

    for x in a:
        print(x)