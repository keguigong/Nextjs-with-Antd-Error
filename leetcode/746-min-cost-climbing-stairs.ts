/**
 * 使用最小花费爬楼梯
 * https://leetcode.cn/problems/min-cost-climbing-stairs/
 */

export function minCostClimbingStairs(cost: number[]): number {
  let prev = 0,
    curr = 0
  for (let i = 2; i <= cost.length; i++) {
    const next = Math.min(curr + cost[i - 1], prev + cost[i - 2])
    prev = curr
    curr = next
  }
  return curr
}

let cost = [10, 15, 20]
console.log(minCostClimbingStairs(cost))