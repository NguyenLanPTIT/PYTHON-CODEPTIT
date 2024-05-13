import functools
class CaThi:
    def __init__(self, id, ngay, tgian, ma):
        if id < 10:
            self.ma = "C00" + str(id)
        elif id < 100:
            self.ma = "C0" + str(id)
        else:
            self.ma = "C" + str(id)
        self.ngay = ngay
        self.tgian = tgian
        self.mathi = ma
        self.gio = int(self.tgian[0:2])
        self.phut = int(self.tgian[3:5])
        self.day = int(self.ngay[0:2])
        self.month = int(self.ngay[3:5])
        self.year = int(self.ngay[6:])
    def __str__(self):
        return self.ma + " " + self.ngay + " " + self.tgian + " " + self.mathi

def compare(a, b):
    # So sánh theo ngày và thời gian thi
    if a.year != b.year:
        return 1 if a.year > b.year else -1
    if a.month != b.month:
        return 1 if a.month > b.month else -1
    if a.day != b.day:
        return 1 if a.day > b.day else -1
    if a.gio != b.gio:
        return 1 if a.gio > b.gio else -1
    if a.phut != b.phut:
        return 1 if a.phut > b.phut else -1
    
    # Nếu cùng giờ, so sánh theo mã ca thi
    return 1 if a.ma > b.ma else -1
file = open("CATHI.in", 'r')
n = int(file.readline().strip())
arr = []
for i in range(n):
    a = file.readline().strip()
    b = file.readline().strip()
    c = file.readline().strip()
    ct = CaThi(i + 1, a, b, c)
    arr.append(ct)
arr.sort(key = functools.cmp_to_key(compare))
for i in arr:
    print(i)