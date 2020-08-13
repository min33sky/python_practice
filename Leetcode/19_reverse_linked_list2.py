# https://leetcode.com/problems/reverse-linked-list-ii/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseBetween(head: ListNode, m: int, n: int) -> ListNode:
    # 예외 처리
    if not head or m == n:
        return head

    root = start = ListNode(None)
    root.next = head

    # 위치를 바꿀 시작 지점까지 포인터 이동하기
    for _ in range(m - 1):
        start = start.next
    end = start.next

    # 종료 위치까지 노드 스위칭 하기
    for _ in range(n - m):
        tmp, start.next, end.next = start.next, end.next, end.next.next
        start.next.next = tmp

    return root.next

