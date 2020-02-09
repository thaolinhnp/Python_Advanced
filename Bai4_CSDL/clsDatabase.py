import sqlite3
class Database():
    def __init__(self, file_db):
        self.conn = sqlite3.connect(file_db)
    def GetAll(self, chuoiSQL, btdk=()):
        cursor = self.conn.execute(chuoiSQL,btdk)
        lst = cursor.fetchall()
        return lst
    def GetOne(self, chuoiSQL, btdk=()):
        cursor = self.conn.execute(chuoiSQL,btdk)
        item = cursor.fetchone()
        return item
    def Execute(self, chuoiSQL, btdk=()):
        cursor = self.conn.execute(chuoiSQL,btdk)
        self.conn.commit()
        return cursor.rowcount
    def DeConnect(self):
        self.conn.close()
