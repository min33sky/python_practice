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
  let rev = null;
  let slow = head;
  let fast = head;

  while (fast && fast.next) {
    fast = fast.next.next;
    // 다중 할당을 통해서 같은 값을 참조 하는 것을 막는다
    [rev, rev.next, slow] = [slow, rev, slow.next];
  }

  // 노드가 홀수 일때는 palindrom에서 정 가운데 노드는 제외한다.
  if (fast) {
    slow = slow.next;
  }

  while (rev && rev.val === slow.val) {
    [slow, rev] = [slow.next, rev.next];
  }

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
