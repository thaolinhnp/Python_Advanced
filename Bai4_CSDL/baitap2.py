from clsQuanLyNV import QuanLyNV
tt = 1
path_db = 'files_db\ql_nhan_vien.db'
qlnv = QuanLyNV(path_db)
while tt == 1:
    print ('Bạn muốn làm gì?')
    print ('1: Hiển thị danh sách phòng')
    print ('2: Thêm phòng mới')
    print ('3: Thêm nhân viên theo phòng')
    print ('4: Hiển thị danh sách nhân viên theo phòng')
    tt = int(input('Chọn chức năng: '))

    if tt == 1:
        DSPhong = qlnv.lstPhong()
        print(DSPhong)
    
    elif tt == 2:
        ten = input('Tên phòng: ')
        chuc_nang = input('Chức năng: ')
        n = qlnv.insertPhong(ten, chuc_nang)
        if n >0:
            print('Thêm phòng thành công')
        else:
            print('Thêm phòng không thành công')

    elif tt == 3:
        id_phong = input('Nhập id phòng muốn thêm nhân viên:')
        ho_ten = input('Họ tên nhân viên: ')
        tuoi = input('Tuổi: ')
        dia_chi = input('Địa chỉ: ')
        luong = float(input('Lương: '))
        n = qlnv.insertNhanVien(ho_ten,tuoi,dia_chi,luong,id_phong)
        if n >0:
            print('Thêm nhân viên thành công')
        else:
            print('Thêm nhân viên không thành công')

    elif tt == 4:
        DSPhong = qlnv.lstPhong()
        lstIdPhong = []
        for item in DSPhong:
            id_phong = item['id']
            lstIdPhong.append(id_phong)
        for id_phong in lstIdPhong:
            print (id_phong)
            print (qlnv.lstNhanVien(id_phong))