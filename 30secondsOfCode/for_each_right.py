# 제공된 함수에 리스트에 모든 요소를 매개변수로 제공하기 (역으로 제공)


def for_each_right(itr, fn):
    for item in itr[::-1]:
        fn(item)


for_each_right([1, 2, 3, 4, 5], print)

