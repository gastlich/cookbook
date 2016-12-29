filename = 'spam.txt'
print(filename.endswith('.txt'))
print(filename.startswith('file:'))
url = 'http://www.python.org'
print(url.startswith('http:'))

import os

filenames = os.listdir('.')
print(filenames)
print(any(name.endswith('.py') for name in filenames))

from urllib.request import urlopen


def read_data(name: str):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()


print(len(read_data('2.1.py')))
print(len(read_data('http://google.com/')))
