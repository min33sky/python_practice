# 리스트에서 Falsy 값을 제거하기

def compact(lst):
    return list(filter(None, lst))


print(compact([0, 1, False, "", 2, 3, 4, 5, "a"]))

