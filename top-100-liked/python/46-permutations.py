# 46. 全排列
# https://leetcode.cn/problems/permutations
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans: List[List[int]] = []

        def backtrace(stored: List[int]):
            if len(stored) == len(nums):
                ans.append(stored)
            else:
                for num in nums:
                    if num not in stored:
                        temp = stored[:]
                        temp.append(num)
                        backtrace(temp)

        backtrace([])
        return ans
