class QuanLyCD():
    def __init__(self, tenCD, caSy, soBH, giaThanh):
        self.tenCD = tenCD
        self.caSy = caSy
        self.soBH = soBH
        self.giaThanh = giaThanh

if __name__ == "__main__":
    dsCD = []
    tt = 1
    while tt == 1:
        tenCD = str(input('Ten CD:'))
        caSy = str(input('Ca sy:'))
        soBH = int(input('So bai hat:'))
        giaThanh = eval(input('Gia thanh:'))
        CD = QuanLyCD(tenCD,caSy,soBH,giaThanh)
        dsCD.append(CD)
        tt = int(input('Tiep tuc nhap (1: co, 0: khong):'))

    if len(dsCD):
        tongGiaThanh = 0
        for item in dsCD:
            print(item.tenCD,' - ',item.caSy,' - ',item.soBH,' - ',item.giaThanh)
            tongGiaThanh += item.giaThanh
        print('Tong Gia Thanh :',tongGiaThanh)
