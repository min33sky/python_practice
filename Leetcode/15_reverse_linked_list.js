/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * 재귀로 풀기
 * @param {ListNode} head
 * @return {ListNode}
 */
// var reverseList = function (head) {
//   function reverse(node, prev = null) {
//     if (!node) {
//       return prev;
//     }

//     [node.next, next] = [prev, node.next];

//     return reverse(next, node);
//   }

//   return reverse(head);
// };

/**
 * 반복으로 풀기
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function (head) {
  let [prev, current] = [null, head];

  while (current) {
    [current.next, current, prev] = [prev, current.next, current];
  }

  return prev;
};
