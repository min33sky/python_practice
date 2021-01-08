def the_most_frequent(lst: list):
    return max(lst, key=lst.count)


print(the_most_frequent(["a", "b", "c", "a", "b", "a"]))
print(the_most_frequent(["a", "a", "bi", "bi", "bi"]))

