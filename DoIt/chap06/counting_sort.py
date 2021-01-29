# 도수 정렬 알고리즘 구현하기

from typing import MutableSequence


def fsort(a: MutableSequence, max: int) -> None:
    """ 도수 정렬(배열 원솟값은 0이상 max이하) """

    n = len(a)                  # 정렬할 배열 a
    f = [0] * (max + 1)         # 누적 도수 분포표 배열 f
    b = [0] * n                 # 작업용 배열 b

    for i in range(n):          # 도수 분포 배열
        f[a[i]] += 1

    for i in range(1, max + 1):  # 누적 도수 분포 배열
        f[i] += f[i - 1]

    for i in range(n - 1, -1, -1):  # 작업용 배열로 이동
        f[a[i]] -= 1
        b[f[a[i]]] = a[i]

    for i in range(n):  # 원본 배열로 복사
        a[i] = b[i]


def counting_sort(a: MutableSequence) -> None:
    """ 도수 정렬 """
    fsort(a, max(a))


if __name__ == "__main__":
    print('도수 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num

    for i in range(num):
        while True:
            x[i] = int(input(f'x[{i}]: '))
            if x[i] >= 0:
                break
    counting_sort(x)

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}]: {x[i]}')
