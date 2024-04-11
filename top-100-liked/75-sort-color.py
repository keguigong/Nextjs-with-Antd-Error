# 75. 颜色分类
# https://leetcode.cn/problems/sort-colors/

from typing import List


def swap(nums: List[int], i: int, j: int):
    nums[i], nums[j] = nums[j], nums[i]


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        zero, two = 0, n - 1
        i = 0
        while i <= two:
            if nums[i] == 0:
                swap(nums, i, zero)
                i += 1
                zero += 1
            elif nums[i] == 1:
                i += 1
            else:
                swap(nums, i, two)
                two -= 1
