# 148. 排序链表
# https://leetcode.cn/problems/sort-lis
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getLength(head: Optional[ListNode]):
    n = 0
    while head:
        n += 1
        head = head.next
    return n


def merge(l1: Optional[ListNode], l2: Optional[ListNode]):
    dummy = ListNode()
    p = dummy
    while l1 and l2:
        if l1.val < l2.val:
            p.next = l1
            l1 = l1.next
        else:
            p.next = l2
            l2 = l2.next
        p = p.next

    p.next = l1 if l1 else l2
    return dummy.next


def cut(head: Optional[ListNode], n: int):
    p = head
    while n > 1 and p:
        p = p.next
        n -= 1
    if not p:
        return None
    next = p.next
    p.next = None
    return next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        n = getLength(head)

        size = 1
        while size < n:
            curr = dummy.next
            tail = dummy

            while curr:
                left = curr
                right = cut(left, size)
                curr = cut(right, size)

                # print("left = {}, right = {}".format(left, right))
                tail.next = merge(left, right)
                # print(tail.next)
                while tail.next:
                    tail = tail.next

            size *= 2

        return dummy.next
