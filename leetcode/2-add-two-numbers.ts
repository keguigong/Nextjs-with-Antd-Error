/**
 * https://leetcode.cn/problems/add-two-numbers/
 */

class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function addTwoNumbers(
  l1: ListNode | null,
  l2: ListNode | null
): ListNode | null {
  let xList = new ListNode(0);
  let pointer = xList;
  let carry = 0;

  while (l1 != null || l2 != null) {
    let x = l1 != null ? l1.val : 0;
    let y = l2 != null ? l2.val : 0;
    let sum = carry + x + y;
    carry = sum - 10 >= 0 ? 1 : 0;
    pointer.next = new ListNode(sum % 10);
    pointer = pointer.next;
    if (l1 != null) l1 = l1.next;
    if (l2 != null) l2 = l2.next;
  }

  if (carry > 0) {
    pointer.next = new ListNode(carry);
  }
  return xList.next;
}

let l1: ListNode = new ListNode(2);
l1.next = new ListNode(4);
l1.next.next = new ListNode(3);

let l2: ListNode = new ListNode(5);
l2.next = new ListNode(6);
l2.next.next = new ListNode(4);

let sum = addTwoNumbers(l1, l2);
console.log(sum);
