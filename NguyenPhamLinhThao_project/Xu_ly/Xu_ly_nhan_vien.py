from Xu_ly.Xu_ly_Database import *

class ql_nhan_vien(Database):
    def __init__(self, file_db):
        Database.__init__(self, file_db)

    def them_tai_khoan(self,hoTen,ngaySinh,diaChi,dienThoai,ngayVaoLam,phongBan,tenDangNhap,matKhau):
        chuoiSQL = 'insert into dsNhanVien \
                    (hoTen,ngaySinh,diaChi,dienThoai,ngayVaoLam,phongBan,tenDangNhap,matKhau) \
                    values (?,?,?,?,?,?,?,?)'
        btdk = (hoTen,ngaySinh,diaChi,dienThoai,ngayVaoLam,phongBan,tenDangNhap,matKhau)
        n = Database.Execute(self,chuoiSQL,btdk=btdk)
        return n

    def dang_nhap(self,tenDangNhap,matKhau):
        chuoiSQL = 'select tenDangNhap, matKhau from dsNhanVien'
        tplTaiKhoan = Database.GetAll(self,chuoiSQL)
        n = 0
        for item in tplTaiKhoan:
            if tenDangNhap == item[0] and matKhau == item[1]:
                n += 1
        return n

    def check_ten_dang_nhap(self, tenDangNhap):
        chuoiSQL = 'select tenDangNhap, matKhau from dsNhanVien where tenDangNhap = (?)'
        DangNhap = Database.GetOne(self,chuoiSQL,(tenDangNhap,))
        return DangNhap

    def ds_nv_theo_phong(self,phongBan):
        chuoiSQL = 'select hoTen, ngaySinh, diaChi, dienThoai, ngayVaoLam from dsNhanVien where phongBan = (?)'
        tplNhanVien = Database.GetAll(self,chuoiSQL,(phongBan,))
        lstNhanVien = []
        for item in tplNhanVien:
            nv = {'hoTen': item[0], 'ngaySinh': item[1], 'diaChi': item[2], 'dienThoai': item[3], 'ngayVaoLam': item[4]}
            lstNhanVien.append(nv)
        return lstNhanVien

    def tim_nhan_vien(self,tenDangNhap):
        chuoiSQL = 'select hoTen, ngaySinh, diaChi, dienThoai, ngayVaoLam, phongBan, tenDangNhap, matKhau \
                    from dsNhanVien where tenDangNhap = (?)'
        NhanVien = Database.GetOne(self,chuoiSQL,(tenDangNhap,))
        return NhanVien

    def cap_nhat_nhan_vien(self,hoTen,ngaySinh,diaChi,dienThoai,ngayVaoLam,phongBan,tenDangNhap):
        chuoiSQL = 'update dsNhanVien set hoTen = ?, ngaySinh = ?, diaChi = ?, dienThoai = ?, ngayVaoLam = ?, phongBan = ? \
                        where tenDangNhap = ?'
        n = Database.Execute(self,chuoiSQL,(hoTen,ngaySinh,diaChi,dienThoai,ngayVaoLam,phongBan,tenDangNhap))
        return n



