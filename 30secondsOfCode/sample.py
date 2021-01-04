# 리스트에서 랜덤으로 요소 선택하기
from random import randint


def sample(lst: list):
    return lst[randint(0, len(lst) - 1)]


print(sample([3, 7, 9, 11]))

