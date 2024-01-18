# 88. 合并两个有序数组
# https://leetcode.cn/problems/merge-sorted-array
from typing import List


class Solution:
    def insert(self, nums: List[int], index: int, value: int):
        n = len(nums)
        for i in range(index, n):
            temp = nums[i]
            nums[i] = value
            value = temp

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = 0
        while p1 < m + n and nums2:
            if p1 + len(nums2) < m + n:
                if nums1[p1] >= nums2[0]:
                    self.insert(nums1, p1, nums2.pop(0))
                    p1 += 1
                else:
                    p1 += 1
            else:
                for num in nums2:
                    self.insert(nums1, p1, num)
                    p1 += 1
                break
