# 24. 两两交换链表中的节点
# https://leetcode.cn/problems/swap-nodes-in-pairs
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(0, head)
        one, two = head, head.next
        pre = dummy
        while one and two:
            next = two.next
            two.next = one
            one.next = next
            pre.next = two

            pre = one
            if not next:
                break
            one = next
            two = next.next

        return dummy.next
