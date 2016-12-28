from operator import itemgetter

rows = [
    {'name': 'Jack', 'salary': 1400, 'age': 21},
    {'name': 'Tom', 'salary': 1400, 'age': 19},
    {'name': 'Mark', 'salary': 1100, 'age': 27},
    {'name': 'Agnes', 'salary': 3200, 'age': 48},
]

assert sorted(rows, key=itemgetter('salary')) == sorted(rows, key=lambda x: x['salary'])
assert sorted(rows, key=itemgetter('age')) == sorted(rows, key=lambda x: x['age'])
assert sorted(rows, key=itemgetter('salary', 'age')) == sorted(rows, key=lambda x: (x['salary'], x['age'],))
