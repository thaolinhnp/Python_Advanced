from Xu_ly.Xu_ly_Database import *

class Lien_he(Database):
    def __init__(self, file_db):
        Database.__init__(self, file_db)

    def them_lien_he(self, tieuDe, noiDung):
        chuoiSQL = 'insert into dsLienHe (tieuDe, noiDung) values (?,?)'
        n = Database.Execute(self, chuoiSQL, (tieuDe,noiDung))
        return n