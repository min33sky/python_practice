# 고정 길이 스택 클래스 구현하기 (collections.deque 사용)


from collections import deque
from typing import Any


class Stack:
    """ 고정 길이 스택 클래스(collections.deque를 사용) """

    def __init__(self, maxlen: int = 256) -> None:
        """ 스택 초기화 """
        self.capacity = maxlen
        self.__stk = deque([], maxlen)

    def __len__(self) -> int:
        """ 스택에 쌓여 있는 데이터 개수를 반환 """
        return len(self.__stk)

    def is_empty(self) -> bool:
        """ 스택이 비어 있는지 판단 """
        return not self.__stk

    def is_full(self) -> bool:
        """ 스택이 가득 차 있는지 판단 """
        return len(self.__stk) == self.__stk.maxlen

    def push(self, value: Any) -> None:
        self.__stk.append(value)

    def pop(self) -> Any:
        return self.__stk.pop()

    def peek(self) -> Any:
        return self.__stk[-1]

    def clear(self) -> None:
        self.__stk.clear()

    def find(self, value: Any) -> Any:
        try:
            return self.__stk.index(value)
        except ValueError:
            return -1

    def count(self, value: Any) -> int:
        return self.__stk.count(value)

    def __contains__(self, value: Any) -> bool:
        return self.count(value)

    def dump(self) -> int:
        print(list(self.__stk))
