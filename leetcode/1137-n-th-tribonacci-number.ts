/**
 * 第 N 个泰波那契数
 * https://leetcode.cn/problems/n-th-tribonacci-number/
 */

export function tribonacci(n: number): number {
  const dp = []
  dp[0] = 0
  dp[1] = 1
  dp[2] = 1
  for (let i = 3; i <= n; i++) {
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
  }
  return dp[n]
}
