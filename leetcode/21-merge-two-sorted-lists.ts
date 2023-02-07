/**
 * 合并两个有序链表
 * https://leetcode.cn/problems/merge-two-sorted-lists/
 */

class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function mergeTwoLists(
  list1: ListNode | null,
  list2: ListNode | null
): ListNode | null {
  let xList = new ListNode();
  let pointer = xList;

  while (list1 != null || list2 != null) {
    if (list1 == null && list2 != null) {
      pointer.next = new ListNode(list2.val);
      list2 = list2.next;
    } else if (list1 !== null && list2 == null) {
      pointer.next = new ListNode(list1.val);
      list1 = list1.next;
    } else if (list1 != null && list2 != null) {
      if (list1.val < list2.val) {
        pointer.next = new ListNode(list1.val);
        list1 = list1.next;
      } else {
        pointer.next = new ListNode(list2.val);
        list2 = list2.next;
      }
    }
    pointer = pointer.next;
  }

  return xList.next;
}

export function getListNode(arr: number[]): ListNode {
  let l = new ListNode();
  let p = l;
  for (let i of arr) {
    p.next = new ListNode(i);
    p = p.next;
  }
  return l.next;
}

let l1 = getListNode([]);
let l2 = getListNode([0]);
let res = [];
let resList = mergeTwoLists(l1, l2);
while (resList != null) {
  res.push(resList.val);
  resList = resList.next;
}
console.log(res);
