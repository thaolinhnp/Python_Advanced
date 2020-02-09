import sqlite3
con = sqlite3.connect('files_db/product.db')

id=int(input('Cho biết ID: '))
chuoiSQL = 'select * from product where id = ?'
cursor = con.execute(chuoiSQL,(id,))
item = cursor.fetchone()
if item == None:
    print('San pham nay ko ton tai')
else:
    chuoiSQL = 'delete from product where id=?'
    cursor = con.execute(chuoiSQL,(id,))
    con.commit
con.close()