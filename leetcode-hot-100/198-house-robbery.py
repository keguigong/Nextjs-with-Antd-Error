# 198. 打家劫舍
# https://leetcode.cn/problems/house-robber
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums)
        dp = [0] * n
        for i in range(n):
            if i == 0:
                dp[i] = nums[0]
            elif i == 1:
                dp[i] = max(nums[0], nums[1])
            else:
                dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
        return dp[-1]
