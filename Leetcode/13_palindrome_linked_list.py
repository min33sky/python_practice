# https://leetcode.com/problems/palindrome-linked-list/
from typing import List
from typing import Deque
from collections import deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head: ListNode) -> bool:
    rev = None
    slow = fast = head

    # 런너를 이용해 역순 연결 리스트 구성
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next

    if fast:
        slow = slow.next

    # 팰린드롬 여부 확인
    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next

    return not rev


# def isPalindrome(head: ListNode) -> bool:

#     q: Deque = deque()

#     if not head:
#         return True

#     node = head

#     # 리스트 변환
#     while node is not None:
#         q.append(node.val)
#         node = node.next

#     # 팰린드롭 판별
#     while len(q) > 1:
#         if q.popleft() != q.pop():
#             return False

#     return True


node1 = ListNode(2)
node2 = ListNode(1)
node3 = ListNode(1)
node4 = ListNode(2)

node1.next = node2
node2.next = node3
node3.next = node4

print(isPalindrome(node1))
