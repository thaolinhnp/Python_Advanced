import re
text = 'There are five apples on the table'
print(re.findall(r'\b\w{5}\b', text))