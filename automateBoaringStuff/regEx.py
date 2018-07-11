import re

phoneNumRegex = re.compile('\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-1556')
print('Phone number found: ' + mo.group())