# 80. 删除有序数组中的重复项 II
# https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 0, 1
        count = 0
        while right < len(nums):
            if nums[left] != nums[right]:
                count = 0
            else:
                count += 1

            if count <= 1:
                left += 1
                nums[left] = nums[right]
            right += 1
        return left + 1
