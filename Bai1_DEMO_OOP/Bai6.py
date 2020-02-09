class GiaoDich():
    def __init__(self, maGD, ngayGD, donGia, soLuong, loai):
        self.maGD = maGD
        self.ngayGD = ngayGD
        self.donGia = donGia
        self.soLuong = soLuong
        self.loai = loai

    def tinh_giao_dich(self):
        return self.donGia * self.soLuong

    def in_giao_dich(self):
        return self.maGD +'-'+ self.ngayGD + '-' + str(self.donGia) + '-' \
              + str(self.soLuong) + '-' + self.loai + '- THANH TIEN:' + str(self.tinh_giao_dich())

class GiaoDichTienTe():
    def __init__(self, maGD, ngayGD, donGia, soLuong, loai, mua):
        self.mua = mua
        GiaoDich.__init__(self, maGD, ngayGD, donGia, soLuong, loai, mua)

    def nhap_giao_dich(self):
        if self.mua:
            return GiaoDich.tinh_giao_dich(self)
        else: 
            return GiaoDich.tinh_giao_dich(self) * 1.05

    def in_giao_dich(self):
        if self.mua:
            return 'GD mua:' + GiaoDich.in_giao_dich(self)
        else:
            return 'GD ban' + GiaoDich.in_giao_dich(self)

if __name__ == "__main__":
    lst_gdv = []
    lst_gdtt = []
    tt = 1
    while tt == 1:
        maGD = input('Nhap ma GD:\t')
        ngayGD = input('Nhap ngay GD:\t')
        soLuong = int(input('Nhap so luong:\t'))
        loaiGD = int(input('Chon loai GD (1: Vang, 2: Tien te):\t'))

        if loaiGD == 1:
            loai = input('Chon loai: 18k/ 24k/ 9999:\t')
            donGia = eval(input('Nhap don gia:\t'))
            gdv = GiaoDich(maGD,ngayGD,donGia,soLuong,loai)
            lst_gdv.append(gdv)

            tong_slv = 0
            tong_tien_vang = 0
            for item in lst_gdv:
                tong_slv += item.soLuong
                tong_tien_vang += item.tinh_giao_dich()
                print(gdv.in_giao_dich())
            print ('Tong so luong:\t',tong_slv)
            print ('Tong tien vang:\t',tong_tien_vang)

        if loaiGD == 2:
            loai = input('Chon loai: USD/ EUR/ AUD:\t')
            donGia = eval(input('Nhap ty gia:\t'))
            mua = True
            mua = input('Ban mua hay ban? (1: mua, 2: ban):\t')
            if mua == 2:
                mua = False
            gdtt = GiaoDichTienTe(maGD,ngayGD,donGia,soLuong,loai,mua)
            lst_gdtt.append(gdtt)

            tong_slt = 0
            tong_tien_te = 0
            for item in lst_gdtt:
                tong_slt += item.soLuong
                tong_tien_te += item.tinh_giao_dich()
                print (gdtt.in_giao_dich())
            print ('Tong so luong:\t',tong_slt)
            print ('Tong tien vang:\t',tong_tien_te)

        tt = (input('Ban co muon tiep tuc giao dich? (1: co, 0: khong)\t'))
