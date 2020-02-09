import json
from thu_vien.nhanvien import NhanVien

f = open('files/dsNhanVien.json')
dsNhanVienGhi = json.load(f)
f.close
dsNhanVien=[]
manv=1
while manv!='':
    manv = input('Nhap Ma Nhan Vien: ')
    if manv!='':
        hoten=input('Nhap ho ten: ')
        diachi=input('Nhap dia chi: ')
        nv = NhanVien(manv,hoten,diachi)
        dsNhanVien.append(nv)

for nv in dsNhanVien:
    dsNhanVienGhi['dsnv'].append(nv.__dict__)
#ghi file
f = open('files/dsNhanVien.json','w')
json.dump(dsNhanVienGhi,f,indent=4)
f.close