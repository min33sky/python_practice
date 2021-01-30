# 이진 검색 트리


from __future__ import annotations
from typing import Any


class Node:
    """ 이진 검색 트리의 노드 """

    def __init__(self, key: Any, value: Any, left: Node = None, right: Node = None) -> None:
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:
    """ 이진 검색 트리 """

    def __init__(self) -> None:
        self.root = None

    def search(self, key: Any) -> Any:
        """ 키가 key인 노드를 검색 """
        p = self.root           # 루트에 주목
        while True:
            if p is None:
                return None     # 검색 실패
            if key == p.key:
                return p.value  # 검색 성공
            elif key < p.key:
                p = p.left
            else:
                p = p.right

    def add(self, key: Any, value: Any) -> bool:
        """ 키가 key이고 값이 value인 노드를 삽입 """

        def add_node(node: Node, key: Any, value: Any) -> None:
            """ node를 루트로 하는 서브트리에 키가 key이고 값이 value인 노드를 삽입 """
            if key == node.key:
                return False        # key가 이진 검색 트리에 이미 존재하므로 추가하지 않는다.
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, value, None, None)
                else:
                    add_node(node.left, key, value)
            else:
                if node.right is None:
                    node.right = Node(key, value, None, None)
                else:
                    add_node(node.right, key, value)

            return True

        if self.root is None:
            self.root = Node(key, value, None, None)
            return True
        else:
            return add_node(self.root, key, value)

    def remove(self, key: Any) -> bool:
        """ 키가 key인 노드를 삭제 """
        p = self.root           # 스캔 중인 노드
        parent = None           # 스캔 중인 노드의 부모 노드
        is_left_child = True    # p는 parent의 왼쪽 자식 노드인지 확인

        # 트리에서 해당 키를 검색
        while True:
            if p is None:               # 더 이상 진행할 수 없으면
                return False            # 그 키는 존재하지 않는다.

            if key == p.key:            # key와 노드 p의 키가 같으면
                break                   # 검색 성공
            else:
                parent = p              # 가지를 내려가기 전에 부모 설정
                if key < p.key:
                    is_left_child = True
                    p = p.left
                else:
                    is_left_child = False
                    p = p.right

        if p.left is None:              # p에 왼쪽 자식이 없으면
            if p is self.root:
                self.root = p.right
            elif is_left_child:
                parent.left = p.right   # 부모의 왼쪽 포인터가 오른쪽 자식을 가리킴
            else:
                parent.right = p.right  # 부모의 오른쪽 포인터가 오른쪽 자식을 가리킴
        elif p.right is None:
            if p is self.root:
                self.root = p.left
            elif is_left_child:
                parent.left = p.left
            else:
                parent.right = p.left
        else:
            parent = p
            left = p.left               # 서브트리 안에서 가장 큰 노드
            is_left_child = True
            while left.right is not None:
                parent = left
                left = left.right
                is_left_child = False

            p.key = left.key            # left의 키를 p로 이동
            p.value = left.value        # left의 데이터를 p로 이동

            if is_left_child:
                parent.left = left.left  # left를 삭제
            else:
                parent.right = left.left

        return True

    def dump(self, reverse=False) -> None:
        """ 덤프(모든 노드를 키의 오름차순으로 출력) """

        def print_subtree(node: Node):
            """ node를 루트로 하는 서브트리의 노드를 키의 오름차순으로 출력 """
            if node is not None:
                print_subtree(node.left)
                print(f'{node.key} {node.value}')
                print_subtree(node.right)

        def print_subtree_rev(node: Node):
            """ 내림차 순으로 """
            if node is not None:
                print_subtree_rev(node.right)
                print(f'{node.key} {node.value}')
                print_subtree_rev(node.left)

        print_subtree_rev(self.root) if reverse else print_subtree(self.root)

    def min_key(self) -> Any:
        """ 가장 작은 키 """
        if self.root is None:
            return None
        p = self.root
        while p.left is not None:
            p = p.left

        return p.key

    def max_key(self) -> Any:
        """ 가장 큰 키 """
        if self.root is None:
            return None
        p = self.root

        while p.right is not None:
            p = p.right

        return p.key
