

from typing import MutableSequence


def bubble_sort(a: MutableSequence) -> None:
    n = len(a)
    k = 0  # 검색 종료 인덱스

    while k < n - 1:
        last = n - 1        # 교환 시작 인덱스
        for j in range(n - 1, k, -1):
            if a[j-1] > a[j]:
                a[j-1], a[j] = a[j], a[j-1]
                last = j    # 가장 마지막에 교환된 곳을 저장
        k = last            # 이 지점 밑으로는 정렬 되었으므로 정렬 하지 않는다.


if __name__ == "__main__":
    print('버블 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    bubble_sort(x)

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')
