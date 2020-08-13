/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} m
 * @param {number} n
 * @return {ListNode}
 */
var reverseBetween = function (head, m, n) {
  // 예외 처리
  if (!head || m === n) return head;

  let root = new ListNode();
  let start = root;
  let end = null;
  root.next = head;

  for (let i = 0; i < m - 1; i++) {
    start = start.next;
  }
  end = start.next;

  for (let i = 0; i < n - m; i++) {
    let tmp = start.next;
    start.next = end.next;
    end.next = end.next.next;
    start.next.next = tmp;
  }

  return root.next;
};
