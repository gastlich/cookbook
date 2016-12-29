line = 'asdf fjdk; afed, fjek, asdaf,    foo'
import re

print(re.split(r'[;,\s]\s*', line))
fields = re.split(r'(;|,|\s)\s*', line)
values = fields[::2]
delimiters = fields[1::2] + ['']
rejoin = ''.join(v + d for v, d in zip(values, delimiters))
print(rejoin)

print(re.split(r'(?:,|;|\s)\s*', line))

