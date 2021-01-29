# 포인터로 연결 리스트 구현하기

from __future__ import annotations
from typing import Any


class Node:
    """ 연결 리스트용 노드 클래스 """

    def __init__(self, data: Any = None, next: Node = None) -> None:
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self) -> None:
        self.no = 0          # 노드의 개수
        self.head = None     # 머리 노드
        self.current = None  # 주목 노드

    def __len__(self) -> int:
        return self.no

    def search(self, data: Any) -> int:
        cnt = 0             # 노드 인덱스
        ptr = self.head

        while ptr is not None:
            if ptr.data == data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = ptr.next

        return -1

    def __contains__(self, data: Any) -> bool:
        return self.search(data) >= 0
