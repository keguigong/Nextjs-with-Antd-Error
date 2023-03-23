/**
 * 打家劫舍
 * https://leetcode.cn/problems/house-robber/
 */

export function rob(nums: number[]): number {
  const len = nums.length
  if (len === 1) return nums[0]
  let p = nums[0],
    q = Math.max.apply(null, nums.slice(0, 2))
  for (let i = 2; i < len; i++) {
    const r = Math.max(p + nums[i], q)
    p = q
    q = r
  }
  return q
}

let nums = [1, 2, 3, 1]
console.log(rob(nums))
