# 주어진 리스트에서 특정 요소의 개수를 구하기


def count_occurences(lst, val):
    return len([x for x in lst if x == val and type(x) == type(val)])


print(count_occurences([1, 1, 2, 1, 2, 3], 1))
