from Xu_ly.Xu_ly_nhan_vien import *

tenDangNhap = 'thien.nk'

xlNhanVien = ql_nhan_vien('du_lieu/qlNhanVien.db')
DangNhap = xlNhanVien.check_ten_dang_nhap(tenDangNhap)
print(DangNhap)