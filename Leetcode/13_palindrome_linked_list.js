/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */

function ListNode(val, next) {
  this.val = val === undefined ? 0 : val;
  this.next = next === undefined ? null : next;
}

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function (head) {
  let rev = null; // 역순 연결 리스트를 위한 노드
  let slow = head; // 중간 까지 이동할 노드
  let fast = head; // 끝 까지 이동할 노드

  while (fast && fast.next) {
    fast = fast.next.next;
    // ! 다중 할당을 통해서 같은 값을 참조 하는 것을 막는다
    [rev, rev.next, slow] = [slow, rev, slow.next];
  }

  // ! 노드가 홀수 일때는 slow 노드가 정가운데 위치하게 되는데
  // ! palindrome에서 정가운데는 의미가 없기 때문에 다음 칸으로 이동한다.
  if (fast) {
    slow = slow.next;
  }

  // 역순 연결 리스트와 값을 비교해가며 palindrome인지 체크
  while (rev && rev.val === slow.val) {
    [slow, rev] = [slow.next, rev.next];
  }

  // rev가 null을 가리키면 모두 같다는 뜻이므로 palindrome이 맞다
  return !rev;
};

const node1 = new ListNode(2);
const node2 = new ListNode(1);
const node3 = new ListNode(1);
const node4 = new ListNode(2);

node1.next = node2;
node2.next = node3;
node3.next = node4;

console.log(isPalindrome(node1));
