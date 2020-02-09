import sqlite3
con = sqlite3.connect('files_db/product.db')

id=int(input('Cho biết ID: '))
chuoiSQL = 'select * from product where id = ?'
cursor = con.execute(chuoiSQL,(id,))
item = cursor.fetchone()
if item == None:
    print('San pham nay ko ton tai')
else:
    name=input('Name: ')
    price=float(input('Price: '))
    amount=float(input('Amount: '))

    chuoiSQL = 'update product set name=?, price=?, amount=? where id=?'
    cursor = con.execute(chuoiSQL,(name, price, amount,id))
    con.commit
con.close()