# 두 리스트에 모두 존재하는 요소를 구하기


def similarity(a, b):
    return [item for item in a if item in b]


print(similarity([1, 2, 3], [1, 2, 4]))

