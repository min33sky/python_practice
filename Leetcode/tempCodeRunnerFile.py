# https://leetcode.com/problems/palindrome-linked-list/
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(head: ListNode) -> bool:

    q: List = []

    if not head:
        return True

    node = head

    # 리스트 변환
    while node is not None:
        q.append(node.val)
        node = node.next

    # 팰린드롭 판별
    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False

    return True


node1 = ListNode(2)
node2 = ListNode(3)
node3 = ListNode(1)
node4 = ListNode(2)

node1.next = node2
node2.next = node3
node3.next = node4

print(isPalindrome(node1))
