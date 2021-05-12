# 고정 길이 큐 클래스 FixedQueue 구현하기

from typing import Any


class FixedQueue:

    class Empty(Exception):
        """ 비어 있는 FixedQueue에서 디큐 또는 피크할 때 내보내는 예외 처리 """
        pass

    class Full(Exception):
        """ 가득 차 있는 FixedQueue에서 인큐할 때 내보내는 예외 처리 """
        pass

    def __init__(self, capacity: int) -> None:
        self.no = 0                     # 현재 데이터 개수
        self.front = 0                  # 맨 앞 원소 커서
        self.rear = 0                   # 맨 뒤 원소 커소
        self.capacity = capacity        # 큐의 크기
        self.que = [None] * capacity    # 큐의 본체

    def __len__(self) -> int:
        return self.no

    def is_empty(self) -> bool:
        return self.no <= 0

    def is_full(self) -> bool:
        return self.no >= self.capacity

    def enque(self, x: Any) -> None:
        if self.is_full():
            raise FixedQueue.Full
        self.que[self.rear] = x
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity:
            self.rear = 0

    def deque(self) -> Any:
        if self.is_empty():
            raise FixedQueue.Empty
        x = self.que[self.front]
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        return x

    def peek(self) -> Any:
        if self.is_empty():
            raise FixedQueue.Empty
        return self.que[self.front]

    def find(self, value: Any) -> Any:
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                return idx
        return -1

    def count(self, value: Any) -> int:
        c = 0
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                c += 1
        return c

    def __contains__(self, value: Any) -> bool:
        return self.count(value)

    def clear(self) -> None:
        self.no = self.front = self.rear = 0

    def dump(self) -> None:
        if self.is_empty():
            print('큐가 비었습니다.')
        else:
            for i in range(self.no):
                print(self.que[(i + self.front) % self.capacity], end='')
            print()