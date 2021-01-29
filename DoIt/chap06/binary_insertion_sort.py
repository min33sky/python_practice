

from typing import MutableSequence


def binary_insertion_sort(a: MutableSequence) -> None:
    n = len(a)
    for i in range(1, n):
        key = a[i]
        pl = 0              # 검색 범위의 맨 앞 원소 인덱스
        pr = i - 1          # 검색 범위의 맨 끝 원소 인덱스

        while True:
            pc = (pl + pr) / 2      # 검색 범위의 가운데 원소 인덱스
            if a[pc] == key:
                break
            elif a[pc] < key:
                pl = pr + 1
            else:
                pr = pc - 1
            if pl > pr:
                break

        pd = pc + 1 if pl <= pr else pr + 1  # 삽입해야 할 위치의 인덱스

        # 해당 위치까지 교환하면서 이동
        for j in range(i, pd, -1):
            a[j] = a[j-1]
        a[pd] = key


if __name__ == "__main__":
    print('이진 삽입 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    binary_insertion_sort(x)

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
