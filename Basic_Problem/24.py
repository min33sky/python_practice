def median(lst: list):
    lst.sort()
    half = int(len(lst) / 2)

    return (lst[half] + lst[-half - 1]) / 2


print(median([1, 2, 3, 4, 5]))
print(median([3, 1, 2, 5, 3]))
print(median([1, 300, 2, 200, 1]))
print(median([3, 6, 20, 99, 10, 15]))

