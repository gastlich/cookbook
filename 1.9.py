a = {
    'x': 1,
    'y': 2,
    'z': 3,
}

b = {
    'w': 2,
    'x': 1,
    'z': 12,
}

print(a.keys() & b.keys())
print(a.keys() - b.keys())
print(a.items() & b.items())
print(a.items())

print({key: a[key] for key in a.keys() - {'z', 'w'}})
