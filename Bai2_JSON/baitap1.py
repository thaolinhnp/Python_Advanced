import urllib.request
import json

path = input('Nhap link:')
#http://dnhoang.laptrinhphp.net/public/api/sach/api-sach
url = urllib.request.urlopen(path)
data = json.loads(url.read().decode('utf-8-sig'))

print('Thong ke:')
tong_so_sach = len(data)
print('Tong so sach:', tong_so_sach)
i = 1
for item in data:
    print(i,'/', item['ten_sach'],', Ngay xuat ban:',item['ngay_xuat_ban'],', Gia bia:',item['gia_bia'])
    i +=1