def all_the_same(lst: list):

    return len(set(lst)) <= 1


print(all_the_same([1, 1, 1]))
print(all_the_same([1, 2, 1]))
print(all_the_same(["a", "a", "a"]))
print(all_the_same([]))

