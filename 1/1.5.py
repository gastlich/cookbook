import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        r = heapq.heappop(self._queue)[-1]
        return r


q = PriorityQueue()
q.push('Test1', 12)
q.push('Test2', 24)
q.push('Test3', 5)
q.push('Test4', 11)
q.push('Test5', 14)
q.push('Test6', -3)

print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
