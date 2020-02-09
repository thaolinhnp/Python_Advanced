import re

ten = input('Nhập tên đăng nhập:\t')

matchObj = re.match(r'^([a-z0-9._]{8,})$', ten, re.M|re.I)

if matchObj:
    print('Hợp lệ')
else:
    print('Không hợp lệ!!')