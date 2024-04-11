# 70. 爬楼梯
# https://leetcode.cn/problems/climbing-stairs


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp = [1] * (n + 1)
        dp[1], dp[2] = 1, 2
        print(dp)
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


print(Solution().climbStairs(3))
