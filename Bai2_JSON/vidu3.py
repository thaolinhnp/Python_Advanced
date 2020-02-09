import json
from thu_vien import nhanvien
dsNhanVien=[]
manv=1
while manv!='':
    manv = input('Nhap Ma Nhan Vien: ')
    if manv!='':
        hoten=input('Nhap ho ten: ')
        diachi=input('Nhap dia chi: ')
        nv = nhanvien.NhanVien(manv,hoten,diachi)
        dsNhanVien.append(nv)

dsNhanVienGhi = {}
dsNhanVienGhi['dsnv']=[]
for nv in dsNhanVien:
    dsNhanVienGhi['dsnv'].append(nv.__dict__)
#ghi file
f = open('files/dsNhanVien.json','w')
json.dump(dsNhanVienGhi,f,indent=4)
f.close