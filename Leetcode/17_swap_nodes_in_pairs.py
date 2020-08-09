# https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 재귀로 풀기
def swapPairs(head: ListNode) -> ListNode:

    if head and head.next:
        temp = head.next

        # 스왑된 값을 받는다
        head.next = swapPairs(temp.next)

        temp.next = head

        return temp

    return head


# 반복으로 풀기
# def swapPairs(head: ListNode) -> ListNode:

#     prev = root = ListNode(None)

#     prev.next = head

#     while head and head.next:

#         temp = head.next
#         head.next = temp.next
#         temp.next = head

#         prev.next = temp

#         head = head.next
#         prev = prev.next.next

#     return root.next

