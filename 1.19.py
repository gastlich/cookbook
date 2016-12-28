nums = range(1, 6)
s = sum(x * x for x in nums)

print(s)

import os

files = os.listdir('.')
if any(name.endswith('.py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python!')

s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

