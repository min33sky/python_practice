# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def oddEvenList(self, head: ListNode) -> ListNode:
    # 예외 처리
    if head is None:
        return None

    # 초기화
    odd = head
    even = head.next
    even_head = head.next

    while even and even.next:
        odd.next, even.next = odd.next.next, even.next.next
        odd, even = odd.next, even.next

    # 홀수 노드의 마지막을 짞수 노드의 헤드에 연결
    odd.next = even_head

    return head

