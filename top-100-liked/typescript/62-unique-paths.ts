/**
 * 不同路径
 * https://leetcode.cn/problems/unique-paths/
 */

export function uniquePaths(m: number, n: number): number {
  const dp: number[][] = new Array(m).fill(new Array(n))
  for (let i = 0; i < n; i++) dp[0][i] = 1
  for (let i = 0; i < m; i++) dp[i][0] = 1
  for (let i = 1; i < m; i++) {
    for (let j = 1; j < n; j++) {
      dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    }
  }
  return dp[m - 1][n - 1]
}

let m = 3,
  n = 7
console.log(uniquePaths(m, n))
