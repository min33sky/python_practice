/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var mergeTwoLists = function (l1, l2) {
  if (!l1 || (l2 && l1.val > l2.val)) {
    [l1, l2] = [l2, l1];
  }
  if (l1) {
    l1.next = mergeTwoLists(l1.next, l2);
  }
  return l1;
};
