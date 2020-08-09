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
var swapPairs = function (head) {
  // 페어가 있을 때만 스왑이 가능하다.
  if (head && head.next) {
    let temp = head.next;
    head.next = swapPairs(temp.next);
    temp.next = head;

    // 페어의 앞쪽 노드를 리턴한다.
    return temp;
  }

  // 페어가 아닐 땐 바로 헤드 노드를 리턴
  return head;
};

/**
 * 반복문 사용
 * @param {ListNode} head
 * @return {ListNode}
 */
// var swapPairs = function (head) {
//   let prev = new ListNode(0);
//   let root = prev;

//   prev.next = head;

//   while (head && head.next) {
//     let temp = head.next;

//     [head.next, temp.next, prev.next] = [temp.next, head, temp];

//     head = head.next;
//     prev = prev.next.next;
//   }

//   return root.next;
// };
