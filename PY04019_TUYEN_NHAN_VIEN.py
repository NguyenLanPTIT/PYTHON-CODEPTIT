class NhanVien:
    count=0
    def __init__(self,ten,lt,th ) :
        NhanVien.count+=1
        self.id=f'TS0{NhanVien.count:01d}'
        self.ten=ten
        self.lt=(lambda x: x if x<=10 else x/10.0)(lt)
        self.th=(lambda x: x if x<=10 else x/10.0)(th)
        self.tong= ((self.lt+self.th)/2.0)
        if self.tong >=9.5: self.xeploai="XUAT SAC"
        elif self.tong>=8 and self.tong<9.5 : self.xeploai="DAT"
        elif self.tong>=5 and self.tong<8 : self.xeploai="CAN NHAC"
        else : self.xeploai="TRUOT"
    def gettong(self):
        return self.tong
    def __str__(self):
        return f"{self.id} {self.ten} {self.tong:.2f} {self.xeploai}"
if __name__ == "__main__":
    a=[]
    for _ in range(int(input())):
        a.append(NhanVien(input(),float(input()),float(input())))
    a.sort(key=lambda x:-x.gettong())
    for i in a:
        print(i)    
    
        
        