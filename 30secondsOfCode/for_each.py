# 제공된 함수에 리스트에 모든 요소를 매개변수로 제공하기


def for_each(itr, fn):
    for el in itr:
        fn(el)


for_each([1, 2, 3], print)

