class DonVi():
    def __init__(self,iddv,ten):
        self.iddv = iddv
        self.ten = ten

class NhanVien():
    def __init__(self,idnv,hoTen,gioiTinh,ngaySinh,cmnd,luong,diaChi,iddv):
        self.idnv = idnv
        self.hoTen = hoTen
        self.gioiTinh = gioiTinh
        self.ngaySinh = ngaySinh
        self.cmnd = cmnd
        self.luong = luong
        self.diaChi = diaChi
        self.iddv = iddv

    def in_thong_tin(self):
        gioi_tinh = ''
        if self.gioiTinh == 'true':
            gioi_tinh = 'Nam'
        else:
            gioi_tinh = 'Nữ'
        return self.idnv + '-' + self.hoTen + '-' + gioi_tinh + '-' + self.ngaySinh \
            + '-' + self.cmnd + '-' + self.luong + '-' + self.diaChi

from xml.dom.minidom import parse
import xml.dom.minidom

# Tao danh sach don vi tu file XML đua vao lst_don_vi:
def dsDonVi(lst_don_vi):
    DOMTree = xml.dom.minidom.parse('files_xml/don_vi.xml')
    collection = DOMTree.documentElement
    don_vi_s = collection.getElementsByTagName('DON_VI')

    for don_vi in don_vi_s:
        if don_vi.hasAttribute('ID') and don_vi.hasAttribute('Ten'):
            dv = DonVi(don_vi.getAttribute('ID'),don_vi.getAttribute('Ten'))
        lst_don_vi.append(dv)
    return lst_don_vi

# Tao danh sach nhan vien tu file XML đua vao lst_nhan_vien:
def dsNhanVien(lst_nhan_vien):
    DOMTree = xml.dom.minidom.parse('files_xml/nhan_vien.xml')
    collection = DOMTree.documentElement
    nhan_vien_s = collection.getElementsByTagName('NHAN_VIEN')

    for nhan_vien in nhan_vien_s:
        nv = NhanVien(nhan_vien.getAttribute('ID'),
                      nhan_vien.getAttribute('Ho_ten'),
                      nhan_vien.getAttribute('Gioi_tinh'),
                      nhan_vien.getAttribute('Ngay_sinh'),
                      nhan_vien.getAttribute('CMND'),
                      nhan_vien.getAttribute('Muc_luong'),
                      nhan_vien.getAttribute('Dia_chi'),
                      nhan_vien.getAttribute('ID_DON_VI')
                     )
        lst_nhan_vien.append(nv)
    return lst_nhan_vien

# Thong ke nhan vien theo don vi:
def thong_ke_don_vi(iddv,lst_nhan_vien):
    tong_nv = 0
    nam = 0
    nu = 0
    for nv in lst_nhan_vien:
        if int(nv.iddv) == iddv:
            print(nv.idnv,' - ',nv.hoTen,' - ',nv.cmnd)
            tong_nv += 1
            if nv.gioiTinh == 'true':
                nam += 1
            else:
                nu += 1
    print('Tổng số nhân viên: ',tong_nv,' - Trong đó: ',nam,' nam, và',nu,' nu')

# Tim kiem nhan vien:
def tim_kiem_nhan_vien(ten,lst_nhan_vien):
    for nv in lst_nhan_vien:
        count = 0
        ten_nv = nv.hoTen.lower()
        if ten_nv.find(ten.lower()) != -1:
            count += 1
            print(nv.idnv,' - ',nv.hoTen,' - ',nv.cmnd)
    if count == 0:
        print('Không tìm thấy nhân viên nào')
        
if __name__ == "__main__":
    lst_don_vi = []
    lst_nhan_vien = []
    lst_don_vi = dsDonVi(lst_don_vi)
    lst_nhan_vien = dsNhanVien(lst_nhan_vien)
    # in danh sach don vi
    for dv in lst_don_vi:
        print(dv.iddv,' - ',dv.ten)
    # in danh sach nhan vien theo don vi
    iddv = int(input('Bạn muốn xem thống kê đơn vị nào (nhập số ID): '))
    thong_ke_don_vi(iddv,lst_nhan_vien)
    # tim kiem nhan vien
    ten = str(input('Nhập tên nhân viên cần tìm:\t'))
    tim_kiem_nhan_vien(ten,lst_nhan_vien)