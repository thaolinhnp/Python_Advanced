import re

image = input('Nhập file Hình ảnh:\t')

matchObj = re.match(r'^([a-z0-9._]{3,})+(\.(jpg|png|gif|bmp))$', image, re.M|re.I)

if matchObj:
    print('Hợp lệ')
else:
    print('Không hợp lệ!!')