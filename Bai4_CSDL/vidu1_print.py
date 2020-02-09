import sqlite3
con = sqlite3.connect('files_db/product.db')
chuoiSQL = 'select id, name, price, amount from product'
cursor = con.execute(chuoiSQL)
for item in cursor:
    print(item)
con.close()