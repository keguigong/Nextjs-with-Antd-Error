/**
 * 两数相加
 * https://leetcode.cn/problems/add-two-numbers/
 */

import { getListNode } from "./21-merge-two-sorted-lists";

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

export let l1 = getListNode([2, 4, 3])
let l2 = getListNode([5, 6, 4])
let sum = addTwoNumbers(l1, l2);
console.log(sum);