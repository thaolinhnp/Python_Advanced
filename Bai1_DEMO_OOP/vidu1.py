#tinh chu vi va dien tich HCN
#HCN CD, CR, CV, DT
#CV = (CD+CR)*2, DT=CD*CR
class HinhChuNhat():
    cd = 0
    cr = 0
    #phuong thuc khoi tao (contructer)
    def __init__(self, _cd, _cr):
        self.cd = _cd
        self.cr = _cr
    def ChuVi(self): # phuong thuc (method) ben trong doi tuong phai co self
        cv = (self.cd + self.cr)*2
        return cv
    def DienTich(self):
        dt = self.cd*self.cr
        return dt

# if __name__ == "__main__":
#     #khai bao doi tuong
#     cd = eval(input('Chieu dai:'))
#     cr = eval(input('Chieu rong:'))
#     hcn = HinhChuNhat(cd,cr)
#     print(hcn.ChuVi())
#     print(hcn.DienTich())
#     #phan biet thuoc tinh (attribute) va phuong thuc (method): method phai co()
#     if hasattr(hcn,'cd'):
#         print(getattr(hcn,'cd'))
#     print(hcn.cd)

if __name__ == "__main__":
    #khai bao doi tuong
    #object vs list
    #giai danh sach hinh chu nhat
    dshcn = []
    tt = 1
    while tt ==1:
        cd = eval(input('Chieu dai:'))
        cr = eval(input('Chieu rong:'))
        hcn = HinhChuNhat(cd,cr)
        dshcn.append(hcn)
        tt=int(input('Ban co muon tiep tuc (1: tt)'))
    
    if len(dshcn):
        for item in dshcn:
            print('cd =',item.cd,';cr =',item.cr
                  ,';cv =',item.ChuVi(),';dt =',item.DienTich())