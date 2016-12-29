text = 'yeah, but no, but yeah, but no , but yeah'
print(text == 'yeah')

print(text.startswith('yeah'))
print(text.endswith('no'))
print(text.find('no'))

date1 = '11/27/2012'
date2 = 'Nov 27, 2012'

import re

if re.match(r'\d+/\d+/\d+', date1):
    print('yes')
else:
    print('no')

if re.match(r'\d+/\d+/\d+', date2):
    print('yes')
else:
    print('no')

datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(date1):
    print('yes')
else:
    print('no')

print(datepat.match(date2))

text = 'TOday is 11/27/2012. Pycon stars 3/13/2013'
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.match('11/27/2012'))
print(list('{}-{}-{}'.format(day, month, year) for month, day, year in datepat.findall(text)))
