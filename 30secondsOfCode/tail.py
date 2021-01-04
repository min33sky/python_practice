# 리스트의 첫번째 요소를 제외하고 리턴하기


def tail(lst: list):
    return lst[1:] if len(lst) > 1 else lst


print(tail([1, 2, 3]))
print(tail([1]))

