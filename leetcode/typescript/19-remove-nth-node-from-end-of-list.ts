/**
 * 删除链表的倒数第 N 个结点
 * https://leetcode.cn/problems/remove-nth-node-from-end-of-list/
 */

import { getListNode } from "./21-merge-two-sorted-lists"

/**
 * Definition for singly-linked list.
 * class ListNode {
 *     val: number
 *     next: ListNode | null
 *     constructor(val?: number, next?: ListNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.next = (next===undefined ? null : next)
 *     }
 * }
 */
class ListNode {
  val: number
  next: ListNode | null
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val
    this.next = next === undefined ? null : next
  }
}

function getListNodeLength(head: ListNode): number {
  let len = 0
  while (head) {
    len++
    head = head.next
  }
  return len
}

export function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
  const len = getListNodeLength(head)
  const result = new ListNode(0, head)

  let pointer = result
  for (let i = 0; i < len - n; i++) {
    pointer = pointer.next
  }
  pointer.next = pointer.next.next
  return result.next
}

let head = getListNode([1, 2])
let n = 1
console.log(removeNthFromEnd(head, n))
