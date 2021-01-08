def easy_unpack(arr: tuple):
    return (arr[0], arr[2], arr[-2])


print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7))
print(easy_unpack((1, 1, 1, 1)) == (1, 1, 1))
print(easy_unpack((6, 3, 7)) == (6, 7, 3))

