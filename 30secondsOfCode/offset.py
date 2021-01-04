# 리스트에서 특정 요소들을 리스트의 뒤로 이동시키기


def offset(lst, offset):
    return lst[offset:] + lst[:offset]


print(offset([1, 2, 3, 4, 5], 2))
print(offset([1, 2, 3, 4, 5], -2))

