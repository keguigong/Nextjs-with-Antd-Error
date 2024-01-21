# 26. 删除有序数组中的重复项
# https://leetcode.cn/problems/remove-duplicates-from-sorted-array
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 0, 1
        while right < len(nums):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
            right += 1
        return left + 1
