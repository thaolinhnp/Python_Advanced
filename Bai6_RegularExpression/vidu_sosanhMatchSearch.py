import re
line = 'the wheels on the bus go round and round, round and round, round and round'

matchObj = re.match(r'round', line, re.M|re.I)

if matchObj:
    print('match --> matchObj.group(): ', matchObj.group())
else:
    print('No match!!')

searchObj = re.search(r'round', line, re.M|re.I)

if searchObj:
    print('search --> searchObj.group(): ', searchObj.group())
else:
    print('Nothing found!!')
