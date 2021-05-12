# 커서로 연결 리스트 구현하기

from __future__ import annotations
from typing import Any


Null = -1


class Node:

    def __init__(self, data=Null, next=Null, dnext=Null) -> None:
        self.data = data        # 데이터
        self.next = next        # 리스트의 뒤쪽 포인터
        self.dnext = dnext      # 프리 리스트의 뒤쪽 포인터


class ArrayLinkedList:
    def __init__(self, capacity: int) -> None:
        self.head = Null
        self.current = Null
        self.max = Null                     # 사용중인 꼬리 레코드
        self.deleted = Null                 # 프리 리스트의 머리 노드
        self.capacity = capacity
        self.n = [Node()] * self.capacity
        self.no = 0

    def __len__(self) -> int:
        return self.no

    def get_insert_index(self):
        """ 다음에 삽입할 레코드의 인덱스를 구함 """
        if self.deleted == Null:            # 삭제 레코드는 존재하지 않음
            if self.max < self.capacity:
                self.max += 1
                return self.max             # 새 레코드를 사용
            else:
                return Null                 # 크기 초과

        else:
            rec = self.deleted
            self.deleted = self.n[rec].dnext    # 프리 리스트에서 맨 앞 rec를 꺼내기
            return rec

    def delete_index(self, idx: int) -> None:
        if self.deleted == Null:            # 삭제 레코드는 존재하지 않음
            self.deleted = idx
            self.n[idx].dnext = Null        # idx를 프리 리스트의 맨 앞에 등록
        else:
            rec = self.deleted
            self.deleted = idx              # idx를 프리 리스트의 맨 앞에 삽입
            self.n[rec].dnext = rec

    def search(self, data: Any) -> int:
        """ data와 값이 같은 노드를 검색 """
        cnt = 0
        ptr = self.head

        while ptr != Null:
            if self.n[ptr].data == data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = self.n[ptr].next          # 뒤쪽 노드에 주목
        return Null

    def __contains__(self, data: Any) -> bool:
        return self.search(data) >= 0

    def add_first(self, data: Any) -> None:
        ptr = self.head                         # 삽입하기 전의 헤드 노드
        rec = self.get_insert_index()
        if rec != Null:
            self.head = self.current = rec      # rec번째 레코드에 삽입
            self.n[self.head] = Node(data, ptr)
            self.no += 1

    def add_last(self, data: Any) -> None:
        if self.head == Null:
            self.add_first(data)
        else:
            ptr = self.head
            while self.n[ptr].next != Null:
                ptr = self.n[ptr].next
            rec = self.get_insert_index()

            if rec != Null:
                self.n[ptr].next = self.current = rec
                self.n[rec] = Node(data)
                self.no += 1

    def remove_first(self) -> None:
        if self.head != Null:
            ptr = self.n[self.head].next
            self.delete_index(self.head)
            self.head = self.current = ptr
            self.no -= 1

    def remove_last(self) -> None:
        if self.head != Null:
            if self.n[self.head].next == None:  # 노드가 1개뿐이라면
                self.remove_first()
            else:
                ptr = self.head                 # 스캔 중인 노드
                pre = self.head                 # 스캔 중인 노드의 앞쪽 노드

                while self.n[ptr].next != Null:
                    pre = ptr
                    ptr = self.n[ptr].next

                self.n[pre].next = Null
                self.delete_index(pre)
                self.current = pre
                self.no -= 1

    def remove(self, p: int) -> None:
        """ 레코드 p를 삭제 """
        if self.head != Null:
            if p == self.head:
                self.remove_first()
            else:
                ptr = self.head

                while self.n[ptr].next != p:
                    ptr = self.n[ptr].next
                    if ptr == Null:
                        return              # p는 존재하지 않음

                self.n[ptr].next = Null
                self.delete_index(ptr)
                self.n[ptr].next = self.n[p].next
                self.current = ptr
                self.no -= 1

    def remove_current_node(self) -> None:
        self.remove(self.current)

    def clear(self) -> None:
        while self.head != Null:
            self.remove_first()
        self.current = Null

    def next(self) -> bool:
        """ 주목 노드를 한 칸 뒤로 이동 """
        if self.current == Null or self.n[self.current].next == Null:
            return False
        self.current = self.n[self.current].next
        return True

    def print_current_node(self) -> None:
        if self.current == Null:
            print('주목 노드가 없습니다.')
        else:
            print(self.n[self.current].data)

    def print(self) -> None:
        ptr = self.head

        while ptr != Null:
            print(self.n[ptr].data)
            ptr = self.n[ptr].next

    def dump(self) -> None:
        """ 배열을 덤프 """
        for i in self.n:
            print(f'[{i}] (i.data) {i.next} {i.dnext}')

    def __iter__(self) -> ArrayLinkedListIterator:
        """ 이터레이터를 반환 """
        return ArrayLinkedListIterator(self.n, self.head)


class ArrayLinkedListIterator:

    def __init__(self, n: int, head: int) -> None:
        self.n = n
        self.current = head

    def __iter__(self) -> ArrayLinkedListIterator:
        return self

    def __next__(self) -> Any:
        if self.current == Null:
            raise StopIteration
        else:
            data = self.n[self.current].data
            self.current - self.n[self.current].next
            return data
