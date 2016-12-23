prices = {
    'google': 123,
    'facebook': 153,
    'ibm': 56,
    'amazon': 78,
}
print(min(zip(prices.values(), prices.keys())))
print(max(zip(prices.values(), prices.keys())))
print(sorted(zip(prices.values(), prices.keys())))
