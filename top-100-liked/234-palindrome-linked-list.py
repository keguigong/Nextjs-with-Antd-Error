# 234. 回文链表
# https://leetcode.cn/problems/palindrome-linked-list
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        n = 0
        p = head

        while p:
            n += 1
            p = p.next

        if n <= 1:
            return True

        p = head
        rvs: Optional[ListNode] = None

        for _ in range(n // 2):
            next = p.next
            p.next = rvs
            rvs = p
            p = next

        if n % 2:
            p = p.next

        while p:
            if p.val != rvs.val:
                return False
            p = p.next
            rvs = rvs.next

        return True
