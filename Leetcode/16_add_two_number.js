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
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function (l1, l2) {
  let root = new ListNode(0);
  let head = root;
  let carry = 0;
  while (l1 || l2 || carry) {
    let sum = 0;

    if (l1) {
      sum += l1.val;
      l1 = l1.next;
    }
    if (l2) {
      sum += l2.val;
      l2 = l2.next;
    }

    let val = parseInt((sum + carry) % 10);
    carry = parseInt((sum + carry) / 10);

    head.next = new ListNode(val);
    head = head.next;
  }

  return root.next;
};

let node1 = new ListNode(2);
let node2 = new ListNode(4);
let node3 = new ListNode(3);

let node4 = new ListNode(5);
let node5 = new ListNode(6);
let node6 = new ListNode(4);

node1.next = node2;
node2.next = node3;

node4.next = node5;
node5.next = node6;

console.log(addTwoNumbers(node1, node4).val);
