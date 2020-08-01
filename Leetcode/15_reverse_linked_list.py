# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 반복 방식
def reverseList(head: ListNode) -> ListNode:
    prev, node = None, head

    while node:
        next, node.next = node.next, prev
        node, prev = next, node

    return prev


# 재귀 방식
# def reverseList(head: ListNode) -> ListNode:
#     def reverse(node: ListNode, prev: ListNode = None):
#         if not node:
#             return prev

#         next, node.next = node.next, prev

#         return reverse(next, node)

#     return reverse(head)


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print(reverseList(node1).val)
