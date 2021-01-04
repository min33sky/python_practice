# 리스트의 매 n번째 요소를 리턴하시오


def every_nth(lst, nth):
    return lst[nth - 1 :: nth]


print(every_nth([1, 2, 3, 4, 5, 6], 2))
