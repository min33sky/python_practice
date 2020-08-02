# https://leetcode.com/problems/add-two-numbers/
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:

    # 두 리스트의 합을 담을 리스트의 노드
    root = head = ListNode(0)
    carry = 0

    while l1 or l2 or carry:
        sum = 0

        if l1:
            sum += l1.val
            l1 = l1.next
        if l2:
            sum += l2.val
            l2 = l2.next

        # (몫, 나머지) : 몫은 자리올림 수
        carry, val = divmod(sum + carry, 10)
        head.next = ListNode(val)
        head = head.next

    return root.next


node1 = ListNode(2)
node2 = ListNode(4)
node3 = ListNode(3)

node4 = ListNode(5)
node5 = ListNode(6)
node6 = ListNode(4)

node1.next = node2
node2.next = node3

node4.next = node5
node5.next = node6


print(addTwoNumbers(node1, node4).val)
