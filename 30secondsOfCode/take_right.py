# 리스트의 끝에서부터 요소 가져오기


def take_right(itr, n=1):
    return itr[-n:]


print(take_right([1, 2, 3]))
print(take_right([1, 2, 3], 2))

