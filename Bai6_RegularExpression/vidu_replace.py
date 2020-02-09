import re

phone = '(08) 38-351056 # This is phone number'

# Delete Python-style comments
num = re.sub(r'#.*$','',phone)
print('Phone Number: ', num)

# Remove anything other than digits
num = re.sub(r'\D','',phone)
print('Phone Number: ', num)
