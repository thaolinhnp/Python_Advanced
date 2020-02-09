from Xu_ly.Xu_ly_Database import *

class ql_phong_ban(Database):
    def __init__(self, file_db):
        Database.__init__(self,file_db)

    def tim_phong_ban(self, phongBan):
        chuoiSQL = 'select phongBan, tenQuanLy, viTri from dsPhongBan'
        tplPhong = Database.GetAll(self, chuoiSQL)
        # lstPhong = []
        for item in tplPhong:
            if phongBan == item[0]:
                phong = {'phongBan': item[0]
                        ,'tenQuanLy': item[1]
                        ,'viTri': item[2]}
            # lstPhong.append(phong)
        return phong
