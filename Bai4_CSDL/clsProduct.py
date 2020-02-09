from clsDatabase import Database
class Product(Database):
    def __init__(self,file_db):
        Database.__init__(self, file_db)
    def LstProduct(self):
        chuoiSQL = 'select id, Name, Price, Amount from Product'
        tplProduct = Database.GetAll(self,chuoiSQL)
        lstProduct = []
        if tplProduct != None:
            for item in tplProduct:
                product = {'id': item[0],'Name': item[1],'Price': item[2],'Amount': item[3]}
                lstProduct.append(product)
        return lstProduct
    def FindProductName(self, _name):
        chuoiSQL = 'select id, Name, Price, Amount from Product where Name like ?'
        dk = '%'+_name+'%'
        tplProduct = Database.GetAll(self,chuoiSQL,(dk,))
        lstProduct = []
        if tplProduct != None:
            for item in tplProduct:
                product = {'id': item[0],'Name': item[1],'Price': item[2],'Amount': item[3]}
                lstProduct.append(product)
        return lstProduct
    def ProductId(self,id):
        chuoiSQL = 'select id, Name, Price, Amount from Product where id = ?'
        item = Database.GetOne(self,chuoiSQL,(id,))
        product = {}
        if item != None:
            product = {'id': item[0],'Name': item[1],'Price': item[2],'Amount': item[3]}
        return product
    def AddProduct(self, Name, Price, Amount):
        chuoiSQL = 'insert into Product(Name,Price,Amount) values (?,?,?)'
        n = Database.Execute(self,chuoiSQL,(Name, Price, Amount))
        return n
    def UpdateProduct(self, id, Name, Price, Amount):
        product = self.ProductId(id)
        if product == None:
            return 0
        chuoiSQL = 'update Product set Name=?, Price=?, Amount=? where id=?'
        n = Database.Execute(self,chuoiSQL,(Name,Price,Amount,id))
        return n
    def DeleteProduct(self,id):
        product = self.ProductId(id)
        if product == None:
            return 0
        chuoiSQL = 'delete from Product where id = ?'
        n = Database.Execute(self,chuoiSQL,(id,))
        return n