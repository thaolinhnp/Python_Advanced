from Xu_ly.Xu_ly_Database import *

class NhomTiVi(Database):
    def __init__(self,file_db):
        Database.__init__(self,file_db)

    def InNhomTiVi(self):
        chuoiSQL = 'select id, MaNhom from tblNhomTiVi'
        lst = Database.getAll(self,chuoiSQL)
        lstTivi = []
        for item in lst:
            # tivi = {'id': item[0], 'MaNhom': item[1]}
            lstTivi.append(item[1])
        return lstTivi

    def ThemNhom(self,MaSo,Ten):
        chuoiSQL = 'insert into tblNhomTiVi (id, MaNhom) values (?,?)'
        n = Database.execute(self,chuoiSQL,(MaSo,Ten))
        return n
