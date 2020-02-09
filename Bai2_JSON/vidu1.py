import urllib.request
import json
path = 'http://dnhoang.laptrinhphp.net/public/api/sach/api-sach'

url = urllib.request.urlopen(path)
data = json.loads(url.read().decode('utf-8-sig'))
for item in data:
    print(item['ten_sach'])