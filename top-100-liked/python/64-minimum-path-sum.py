# 64. 最小路径和
# https://leetcode.cn/problems/minimum-path-sum
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid[0]), len(grid)
        dp = [[0] * m for _ in range(0, n)]
        dp[0][0] = grid[0][0]

        for i in range(1, m):
            dp[0][i] = dp[0][i - 1] + grid[0][i]

        for j in range(1, n):
            dp[j][0] = dp[j - 1][0] + grid[j][0]

        for i in range(1, m):
            for j in range(1, n):
                dp[j][i] = min(dp[j][i - 1], dp[j - 1][i]) + grid[j][i]

        return dp[-1][-1]
