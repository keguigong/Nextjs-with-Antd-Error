/**
 * 斐波那契数
 * https://leetcode.cn/problems/fibonacci-number/
 */

export function fib(n: number): number {
  const dp = []
  dp[1] = 1
  dp[2] = 2
  for (let i = 3; i <= n; i++) {
    dp[i] = dp[i - 1] + dp[i - 2]
  }
  return dp[n]
}

console.log(fib(10))
