my_list = [1, 4, -5, 10, -7, 2, 3, -1]
print([n for n in my_list if n > 0])
print([n for n in my_list if n < 0])
pos = (n for n in my_list if n > 0)
print(list(pos))

values = ['1', '2', '-3', '-', '4', 'N/A', '5']


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


ivals = list(filter(is_int, values))

import math

[math.sqrt(n) for n in my_list if n > 0]
clip_neg = [n if n > 0 else 0 for n in my_list]
print(clip_neg)
clip_pos = [n if n < 0 else 0 for n in my_list]
print(clip_pos)

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5418 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

counts = [0, 3, 10, 4, 1, 7, 6, 1]

from itertools import compress

more5 = [n > 5 for n in counts]
print(list(compress(rows, more5)))
