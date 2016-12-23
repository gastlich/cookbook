record = '..................100            ........513.25        ..........'
print(record[18:21], record[41:47])
SHARES = slice(18, 21)
PRICE = slice(41, 47)

cost = float(record[SHARES]) * float(record[PRICE])
print(cost)

a = slice(5, 20, 2)
print(slice.start, slice.stop, slice.step)

word = 'Hello world'
word_slice = a.indices(len(word))
for i in range(*word_slice):
    print(word[i])
