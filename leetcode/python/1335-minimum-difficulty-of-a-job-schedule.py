# 1335. 工作计划的最低难度
# https://leetcode.cn/problems/minimum-difficulty-of-a-job-schedule/

from math import inf
from typing import List


class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            return -1
        dp = [[0x3F3F3F3F] * (d + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            for day in range(1, d + 1):
                mostDifficult = 0
                for k in range(i, 0, -1):
                    mostDifficult = max(mostDifficult, jobDifficulty[k - 1])
                    dp[i][day] = min(dp[i][day], dp[k - 1][day - 1] + mostDifficult)
        return -1 if dp[n][d] >= inf else dp[n][d]
