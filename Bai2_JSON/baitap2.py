import urllib.request
import json

path = input('Nhap link:')
#http://dnhoang.laptrinhphp.net/public/api/sach/sach-noi-bat
url = urllib.request.urlopen(path)
data = json.loads(url.read().decode('utf-8-sig'))
# print(data[0].keys())

top = int(input('Top noi bat:'))
print('--- Danh sách ',top, 'sach noi bat ---')
i = 1
for item in data:
    while i <= top:
        print(i,'/', item['ten_sach']
            ,'\t, Tac gia:',item['id_tac_gia']
            ,'\n- Ngay xuat ban:',item['ngay_xuat_ban']
            ,'\t, Gia bia:',item['gia_bia']
            ,'\n, Gioi thieu:',item['gioi_thieu'][:200])
        i += 1