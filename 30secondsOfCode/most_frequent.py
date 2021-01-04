# 가장 빈번한 요소를 찾아라


def most_frequent(list: list):
    return max(set(list), key=list.count)


print(most_frequent([1, 2, 1, 2, 3, 2, 1, 4, 2]))

