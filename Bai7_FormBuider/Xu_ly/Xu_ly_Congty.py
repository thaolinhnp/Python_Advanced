from Xu_ly.Xu_ly_Database import *

class CongTy(Database):
    def __init__(self,file_db):
        Database.__init__(self,file_db)

    def ThongTinCongTy(self):
        chuoiSQL = 'select id, tenCongTy, maSo, dienThoai, diaChi, email from tblCongTy'
        item = Database.getOne(self, chuoiSQL)
        cty = {'Id': item[0], 'tenCongTy': item[1], 'maSo': item[2]
              ,'dienThoai': item[3], 'diaChi': item[4], 'email': item[5]}
        return cty

    def CapNhatCongty(self, tenCongTy, maSo, dienThoai, diaChi, email):
        chuoiSQL = 'update tblCongTy set tenCongTy =?, maSo =?, dienThoai =?, diaChi =?, email =?'
        n = Database.execute(self, chuoiSQL, btdk= (tenCongTy, maSo, dienThoai, diaChi, email))
        return n
