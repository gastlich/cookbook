def dedupe(l):
    seen = set()
    for val in l:
        if val not in seen:
            yield val
            seen.add(val)


print(list(dedupe([1, 4, 6, 2, 1, 4, 5])))


def hash_dedupe(l, key=None):
    seen = set()
    for item in l:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [{'x': 1, 'y': 2}, {'x': 2, 'y': 1}, {'x': 1, 'y': 2}]
print(list(
    hash_dedupe(a, key=lambda d: (d['x'], d['y']))
))
