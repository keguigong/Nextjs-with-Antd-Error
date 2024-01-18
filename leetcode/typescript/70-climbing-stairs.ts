/**
 * 爬楼梯
 * https://leetcode.cn/problems/climbing-stairs/
 */

// 空间复杂父为O(1)
export function climbStairs(n: number): number {
  let p = 0,
    q = 0,
    r = 1
  for (let i = 1; i <= n; i++) {
    p = q
    q = r
    r = p + q
  }
  return r
}

console.log(climbStairs(4))
