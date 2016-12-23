from collections import Counter

words = ['weasel', 'near', 'controller', 'controller', 'blinks', 'volcano', 'headache', 'alcoholic', 'alcoholic',
         'alcoholic', 'bluster', 'blaster', 'fornicator']

words_count = Counter(words)
print(words_count)
print(words_count.most_common(3))
print(words_count['weasel'])

more_words = ['licker', 'duel', 'narcotic', 'blueprint', 'recent', 'mix', 'decode', 'baloney', 'expert', 'controller']
words_count.update(more_words)
print(words_count.most_common(3))

a = Counter(words)
b = Counter(more_words)

print(a + b)
print(a - b)
print(a & b)
print(a | b)
