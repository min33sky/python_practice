from functools import reduce
from operator import getitem


def get(d, selectors):
    return reduce(getitem, selectors, d)


users = {"freddy": {"name": {"first": "fred", "last": "smith"}, "postIds": [1, 2, 3]}}

print(get(users, ["freddy", "name", "last"]))  # 'smith'
print(get(users, ["freddy", "postIds", 1]))  # 2

