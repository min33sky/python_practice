def index_power(lst: list, num: int):
    if len(lst) <= num:
        return -1

    return lst[num] ** num


print(index_power([1, 2, 3, 4], 2))
print(index_power([1, 3, 10, 100], 3))
print(index_power([0, 1], 0))
print(index_power([1, 2], 3))

