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
var reverseList = function (head) {
  // 리스트를 순회하는 재귀 함수
  function reverse(current, prev = null) {
    // 리스트 순회가 끝났으므로 가장 마지막 노드를 리턴한다.
    if (!current) return prev;

    // 노드를 역순으로 뒤집는다. (prev <- current)
    [current.next, prev, current] = [prev, current, current.next];

    // 재귀 호출
    return reverse(current, prev);
  }

  return reverse(head);
};

/**
 * 반복으로 풀기
 * @param {ListNode} head
 * @return {ListNode}
 */
// var reverseList = function (head) {
//   let [prev, current] = [null, head];

//   while (current) {
//     [current.next, current, prev] = [prev, current.next, current];
//   }

//   return prev;
// };
