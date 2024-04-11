# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack = []
        dummy = ListNode(0, head)
        curr = dummy
        while curr:
            stack.append(curr)
            curr = curr.next

        for _ in range(n):
            stack.pop()

        prev = stack[-1]
        prev.next = prev.next.next

        return dummy.next
