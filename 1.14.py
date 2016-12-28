from operator import attrgetter


class User:
    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return 'User({})'.format(self.id)


users = [User(3), User(5), User(4), User(1), User(2)]
assert sorted(users, key=lambda u: u.id) == sorted(users, key=attrgetter('id'))
