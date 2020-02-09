from clsDatabase import Database

class QuanLyNV(Database):
    def __init__(self,file_db):
        Database.__init__(self,file_db)

    def lstPhong(self):
        chuoiSQL = 'select id, ten, chuc_nang from PHONG'
        tplPhong = Database.GetAll(self,chuoiSQL)
        lstPhong = []
        if tplPhong != None:
            for item in tplPhong:
                phong = {'id': item[0], 'ten': item[1], 'chuc_nang': item[2]}
                lstPhong.append(phong)
        return lstPhong

    def lstNhanVien(self,id_phong):
        chuoiSQL = 'select id,ho_ten,tuoi,dia_chi,luong,id_phong from NHAN_VIEN where id_phong = ?'
        tplNhanVien = Database.GetAll(self,chuoiSQL,(id_phong,))
        lstNhanVien = []
        if tplNhanVien != None:
            for item in tplNhanVien:
                nhanvien = {'id': item[0]
                           ,'ho_ten': item[1]
                           ,'tuoi': item[2]
                           ,'dia_chi': item[3]
                           ,'luong': item[4]
                           ,'id_phong': item[5]}
                lstNhanVien.append(nhanvien)
        return lstNhanVien

    def insertPhong(self,ten, chuc_nang):
        chuoiSQL = 'insert into PHONG (ten, chuc_nang) values (?,?)'
        n = Database.Execute(self,chuoiSQL,(ten,chuc_nang))
        return n

    def insertNhanVien(self,ho_ten,tuoi,dia_chi,luong,id_phong):
        chuoiSQL = 'insert into NHAN_VIEN (ho_ten,tuoi,dia_chi,luong,id_phong) values (?,?,?,?,?)'
        n = Database.Execute(self,chuoiSQL,(ho_ten,tuoi,dia_chi,luong,id_phong))
        return n
