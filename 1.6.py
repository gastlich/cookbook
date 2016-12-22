from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(3)
d['b'].append(4)
print(d)

d = defaultdict(set)
d['a'].add(2)
d['a'].add(2)
print(d)
print(d['c'])
print(d)

names = ['Jacek', 'Aga', 'Marek', 'Aga', 'Jacek']
points = [12, 14, 5, 10, 5]
d = defaultdict(list)

for key, value in zip(names, points):
    d[key].append(value)
print(d)
