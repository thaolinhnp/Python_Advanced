import re
line = 'the wheels on the bus go round and round, round and round, round and round'

matchObj = re.match(r'(.*) go (.*?) .*', line, re.M|re.I)

if matchObj:
    print('matchObj.group(): ', matchObj.group())
    print('matchObj.group(1): ', matchObj.group(1))
    print('matchObj.group(2): ', matchObj.group(2))
    print('matchObj.groups :', matchObj.groups())
else:
    print('No match!!')