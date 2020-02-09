import json
f = open('files/QLCT_1.json', encoding='utf-8')
data = json.load(f) # doc tu file thi load, doc tu web la loads

cong_ty = data['CONG_TY'][0]
don_vi = data['DON_VI']

tongnv = 0
for item in don_vi:
    tongnv += int(item['So_Nhan_vien'])

print('Ten cong ty:', cong_ty['Ten'])
print('Dia chi:', cong_ty['Dia_chi'])
print('Tong so nhan vien:', tongnv)
print('--- Thong ke so nhan vien theo don vi ---')

for item in don_vi:
    print(str(item['ID']),'/ Ten don vi:',item['Ten'])
    print('\t- So nhan vien:', item['So_Nhan_vien'])
    print('\t- Ty le:', item['Ty_le'],'%')