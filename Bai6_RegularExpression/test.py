import re

ngay = '25/06/1991'

matchObj = re.match(r'^([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{4}$', ngay, re.M|re.I)

print(matchObj)
print(matchObj.group())

if matchObj:
    print('Hợp lệ')
else:
    print('Không hợp lệ!!')