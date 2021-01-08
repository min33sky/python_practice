def even_the_last(lst: list):
    if not lst:
        return 0
    return sum(lst[::2] * lst[-1])


print(even_the_last([0, 1, 2, 3, 4, 5]) == 30)
print(even_the_last([1, 3, 5]) == 30)
print(even_the_last([6]) == 36)
print(even_the_last([]) == 0)

