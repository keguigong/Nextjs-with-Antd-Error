"""
55. 跳跃游戏
https://leetcode.cn/problems/jump-game
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, mostJumped = len(nums), 0
        for i in range(n):
            if i <= mostJumped:
                mostJumped = max(mostJumped, i + nums[i])
                if mostJumped >= n - 1:
                    return True
        return False
