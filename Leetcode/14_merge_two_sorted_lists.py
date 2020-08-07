# https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:

    # 리스트1이 None이거나 리스트1의 값이 리스트2보다 클 때 Swap
    if not l1 or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1
    # 다음 노드를 찾기 위해 재귀 호출
    if l1:
        l1.next = mergeTwoLists(l1.next, l2)

    return l1


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(4)
node4 = ListNode(1)
node5 = ListNode(3)
node6 = ListNode(4)

node1.next = node2
node2.next = node3

node4.next = node5
node5.next = node6

print(mergeTwoLists(node1, node4))
