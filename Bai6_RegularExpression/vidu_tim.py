import re
lstTiVi=['Tivi LG 49','Tivi SamSung 49','Tivi Sony 49','Tivi Toshiba 49', 'Tivi LG 50', 'Tivi LG 32']
noidungtim = input('Ban muon tim gi: ')
lstKq = []
for item in lstTiVi:
    matchObj = re.match(r'(.*)' + noidungtim + '(.*)', item, re.M|re.I)
    if matchObj:
        lstKq.append(item)

if len(lstKq)>0:
    print(lstKq)
else:
    print('Khong tim thay')