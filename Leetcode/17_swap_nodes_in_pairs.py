# https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 재귀로 풀기
def swapPairs(head: ListNode) -> ListNode:

    if head and head.next:
        p = head.next
        # 스왑된 값 리턴 받음
        head.next = swapPairs(p.next)
        p.next = head
        return p

    return head


# 반복으로 풀기
# def swapPairs(head: ListNode) -> ListNode:

#     root = prev = ListNode(None)

#     prev.next = head

#     while head and head.next:

#         b = head.next
#         head.next = b.next
#         b.next = head

#         prev.next = b

#         head = head.next
#         prev = prev.next.next

#     return root.next
