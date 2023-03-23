/**
 * 打家劫舍 II
 * https://leetcode.cn/problems/house-robber-ii/
 */

export function rob(nums: number[]): number {
  const len = nums.length
  if (len === 1) return nums[0]
  if (len === 2) return Math.max.apply(null, nums)
  return Math.max(_rob(nums.slice(0, len - 1)), _rob(nums.slice(1, len)))

  function _rob(nums: number[]): number {
    const len = nums.length
    let p = nums[0],
      q = Math.max.apply(null, nums.slice(0, 2))
    for (let i = 2; i < len; i++) {
      const r = Math.max(p + nums[i], q)
      p = q
      q = r
    }
    return q
  }
}

let nums = [2, 3, 2]
console.log(rob(nums))
