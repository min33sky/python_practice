# 셀 정렬 알고리즘 구현하기

from typing import MutableSequence


def shell_sort(a: MutableSequence) -> None:
    n = len(a)
    h = n // 2
    while h > 0:
        for i in range(h, n):
            j = i - h       # 앞 쪽 그룹
            tmp = a[i]
            while j >= 0 and a[j] > tmp:
                a[j + h] = a[j]
                j -= h
            a[j+h] = tmp    # h를 다시 더해서 원래 인덱스로 복귀시킨다
        h //= 2


if __name__ == "__main__":
    print('셸 삽입 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    shell_sort(x)

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
