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
  if (head === null || head.next === null) return true;
  let slow = head;
  let fast = head;

  while (fast.next !== null && fast.next.next !== null) {
    slow = slow.next;
    fast = fast.next.next;
  }
};

function reverseList(head) {
  let pre = null;
  let next = null;
  while (head !== null) {
    next = head.next;
    head.next = pre;
    pre = head;
    head = next;
  }
  return pre;
}

const node1 = new ListNode(2);
const node2 = new ListNode(1);
const node3 = new ListNode(1);
const node4 = new ListNode(2);

node1.next = node2;
node2.next = node3;
node3.next = node4;

console.log(isPalindrome(node1));
