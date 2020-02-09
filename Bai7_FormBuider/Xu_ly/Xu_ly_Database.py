import sqlite3
class Database():
    def __init__(self, file_db):
        self.con = sqlite3.connect(file_db)

    def getAll(self, chuoiSQL, btdk=()):
        cursor = self.con.execute(chuoiSQL,btdk)
        ds = cursor.fetchall()
        return ds

    def getOne(self, chuoiSQL, btdk=()):
        cursor = self.con.execute(chuoiSQL,btdk)
        item = cursor.fetchone()
        return item

    def execute(self, chuoiSQL, btdk=()):
        cursor = self.con.execute(chuoiSQL,btdk)
        self.con.commit
        return cursor.rowcount

    def deConnect(self):
        self.con.close()