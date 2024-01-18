# 27. 移除元素
# https://leetcode.cn/problems/remove-element/
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        update_i, read_i = 0, 0
        while read_i < len(nums):
            if nums[read_i] != val:
                nums[update_i] = nums[read_i]
                update_i += 1
            read_i += 1
        return update_i
