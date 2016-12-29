import heapq

warehouse = [
    {'name': 'Lamp', 'price': 23},
    {'name': 'Bed', 'price': 124},
    {'name': 'Wardrobe', 'price': 56},
    {'name': 'Carpet', 'price': 10},
]

print(heapq.nlargest(2, warehouse, lambda x: x['price']))
print(heapq.nsmallest(2, warehouse, lambda x: x['price']))

nums = [1, 4, 5, -23, 23, -123, -1, 4523, 230]
heap = list(nums)
heapq.heapify(heap)
print(heap)
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
