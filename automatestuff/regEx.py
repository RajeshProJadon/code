import re

phoneNumRegex = re.compile('(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-1556')
print('Phone number found: ' + mo.group())
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.groups())
areacode, mainnumber = mo.groups()
print(areacode, mainnumber)

phoneNumRegexp = re.compile('(\(\d\d\d\)) (\d\d\d\-\d\d\d\d)')
mob = phoneNumRegexp.search('My phone number is (415) 555-4242')
print(mob.group(1))
print(mob.group(2))

heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey')
print(mo1.group())

mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())

batRegex = re.compile('Bat(man|mobile|copter|bat)')
mobat = batRegex.search('Batmobile lost a wheel')
print(mobat.group())
print(mobat.group(1))

