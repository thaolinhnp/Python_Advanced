import sqlite3
con = sqlite3.connect('files_db/product.db')

name=input('Name: ')
price=float(input('Price: '))
amount=float(input('Amount: '))

chuoiSQL = 'insert into product (name, price, amount) values (?,?,?)'
cursor = con.execute(chuoiSQL,(name,price,amount))
con.commit
con.close()