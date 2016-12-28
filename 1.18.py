from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber(addr='Przemysl', joined='7/10/2012')
print(sub.addr)
print(sub)
print(len(sub))
print(*sub)

Record = namedtuple('Record', ['shares', 'name', 'price'])
rec = Record(12, 'Google', 342)


def calculate_record(record: Record) -> float:
    return record.shares * record.price


print(calculate_record(rec))

record_prototype = Record(0, '', 0)


def dict_to_record(d):
    return record_prototype._replace(**d)


record = {'shares': 15, 'name': 'Facebook', 'price': 124}
print(dict_to_record(record))
