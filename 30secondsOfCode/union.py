# 두 리스트의 합집합 구하기 (중복 제외)


def union(a: list, b: list):
    return list(set(a + b))


print(union([1, 2, 3], [2, 3, 4]))

