# 45. 跳跃游戏 II
# https://leetcode.cn/problems/jump-game-ii


from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        https://leetcode.cn/problems/jump-game-ii/solutions/230241/tiao-yue-you-xi-ii-by-leetcode-solution/?envType=study-plan-v2&envId=top-100-liked
        """
        # class Solution:
        #     def jump(self, nums: List[int]) -> int:
        #         n = len(nums)
        #         dp = [10001] * n
        #         dp[0] = 0
        #         for i in range(0, n):
        #             if dp[i] < 10001:
        #                 for jump in range(1, nums[i] + 1):
        #                     if i + jump < n:
        #                         dp[i + jump] = min(dp[i + jump], dp[i] + 1)
        #         return dp[-1]
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step
