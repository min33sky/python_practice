# 커서로 연결 리스트 구현하기

from __future__ import annotations


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
        if self.deleted == Null:            # 삭제 레코드가 존재하지 않음
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
        if self.deleted == Null:            # 삭제 레코드가 존재하지 않음
            self.deleted = idx
            self.n[idx].dnext = Null        # idx를 프리 리스트의 맨 앞에 등록
        else:
            rec = self.deleted
            self.deleted = idx
            self.n[rec].dnext = rec
