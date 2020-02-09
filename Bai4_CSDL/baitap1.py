from clsProduct import Product
tt = 1
path_db = 'files_db\product.db'
product = Product(path_db)

while tt==1:
    print ('Bạn muốn làm gì?')
    print ('1: Hiển thị danh sách sản phẩm')
    print ('2: Tìm kiếm sản phẩm theo tên')
    print ('3: Thêm sản phẩm mới')
    print ('4: Cập nhật sản phẩm')
    print ('5: Xóa sản phẩm')
    tt = int(input('Chọn chức năng: '))
    if tt == 1:
        DSSanPham = product.LstProduct()
        print(DSSanPham)
    elif tt == 2:
        name = input('Name: ')
        DSSanPham = product.FindProductName(name)
        print(DSSanPham)
    elif tt == 3:
        Name = input('Name: ')
        Price = float(input('Price: '))
        Amount = int(input('Amount: '))
        n = product.AddProduct(Name,Price,Amount)
        if n >0:
            print('Thêm thành công')
        else:
            print('Thêm không thành công')
    elif tt == 4:
        id = int(input('id: '))
        Name = input('Name: ')
        Price = float(input('Price: '))
        Amount = int(input('Amount: '))
        n = product.UpdateProduct(id,Name,Price,Amount)
        if n >0:
            print('Cập nhật thành công')
        else:
            print('Cập nhật không thành công')
    elif tt == 5:
        id = int(input('id: '))
        n = product.DeleteProduct(id)
        if n >0:
            print('Xóa thành công')
        else:
            print('Xóa không thành công')
    tt= int(input('Bạn có muốn tiếp tục? (1: có, 2: không)'))