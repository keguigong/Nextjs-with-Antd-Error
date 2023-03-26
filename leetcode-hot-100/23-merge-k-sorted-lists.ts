/**
 * 合并 K 个升序链表
 * https://leetcode.cn/problems/merge-k-sorted-lists/
 */

export function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
  let ans: ListNode = null
  for (let i = 0; i < lists.length; i++) {
    ans = mergeTwoLists(ans, lists[i])
  }
  return ans
}

class ListNode {
  val: number
  next: ListNode | null
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val
    this.next = next === undefined ? null : next
  }
}

function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
  let xList = new ListNode()
  let pointer = xList

  while (list1 != null || list2 != null) {
    if (list1 == null && list2 != null) {
      pointer.next = new ListNode(list2.val)
      list2 = list2.next
    } else if (list1 !== null && list2 == null) {
      pointer.next = new ListNode(list1.val)
      list1 = list1.next
    } else if (list1 != null && list2 != null) {
      if (list1.val < list2.val) {
        pointer.next = new ListNode(list1.val)
        list1 = list1.next
      } else {
        pointer.next = new ListNode(list2.val)
        list2 = list2.next
      }
    }
    pointer = pointer.next
  }

  return xList.next
}
