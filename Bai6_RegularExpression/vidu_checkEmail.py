import re

email = input('Nhập địa chỉ email:\t')

matchObj = re.match(r'^[a-z0-9._]+@[a-z0-9._]+\.[a-z]{2,}$', email, re.M|re.I)

if matchObj:
    print('Hợp lệ')
else:
    print('Không hợp lệ!!')