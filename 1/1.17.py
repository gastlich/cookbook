prices = {
    'A': 200,
    'B': 250,
    'C': 400,
    'D': 270,
    'E': 150,
}

p = {k: v for k, v in prices.items() if v > 200}
print(p)
print(dict((k, v) for k, v in prices.items() if v > 200))

tech = {'A', 'C', 'D'}
p = {k: v for k, v in prices.items() if k in tech}
print(p)
p2 = {k: prices[k] for k in prices.keys() & tech}
print(p2)
