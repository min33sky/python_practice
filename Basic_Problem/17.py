def absolute_sorting(arr: tuple):
    return sorted(arr, key=abs)


print(absolute_sorting((-20, -5, 10, 15)))
print(absolute_sorting((1, 2, 3, 0)))
print(absolute_sorting((-1, -2, -3, 0)))

