# 256 粉刷房子
# https://leetcode.cn/problems/paint-house/

from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        dp = [[0, 0, 0] for _ in range(n)]
        dp[0] = costs[0]
        for i in range(1, n):
            cost = costs[i]
            dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + cost[0]
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + cost[1]
            dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + cost[2]

        return min(dp[-1])
