# 78. 子集
# https://leetcode.cn/problems/subsets

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans: List[List[int]] = []

        def backtrace(begin: int, stored: List[int], n: int):
            if len(stored) == n:
                ans.append(stored)
            elif begin < len(nums):
                for i in range(begin, len(nums)):
                    temp = stored[:]
                    temp.append(nums[i])
                    backtrace(i + 1, temp, n)

        for length in range(len(nums) + 1):
            backtrace(0, [], length)

        return ans
