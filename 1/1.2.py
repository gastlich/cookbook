def drop_first_last(grades):
    first, *middle, last = grades
    return middle


print(drop_first_last([1, 2, 3, 4]))

name, email, *phone_numbers = ('Jack', 'test@test.pl', '0234023454', '123123123')
print(phone_numbers)

records = [
    ('foo', 2, 1),
    ('bar', 4),
    ('foo', 5, 3),
]

for tag, *args in records:
    print(tag, args)

line = 'a:b:c:asdf/asdf/asdf'
a, *fields, path = line.split(':')
print(a, path)

data = ['Google', 10.5, 91.4, (2012, 12, 1)]
name, *_, (year, *_) = data
print(name, year)


def sum(l):
    head, *tail = l
    return head + sum(tail) if tail else head


print(sum([1, 2, 4, 5]))
