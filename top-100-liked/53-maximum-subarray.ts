/**
 * 最大子数组和
 * https://leetcode.cn/problems/maximum-subarray/
 */

export function maxSubArray(nums: number[]): number {
  let p = 0,
    q = nums[0]
  for (let i = 0; i < nums.length; i++) {
    p = Math.max(p + nums[i], nums[i])
    q = Math.max(p, q)
  }

  return q
}

let nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
console.log(maxSubArray(nums))
