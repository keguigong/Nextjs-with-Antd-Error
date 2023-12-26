/**
 * 560. 和为 K 的子数组
 * https://leetcode.cn/problems/subarray-sum-equals-k/?envType=study-plan-v2&envId=top-100-liked
 */

export function subarraySum(nums: number[], k: number): number {
  let res = 0
  for (let left = 0; left < nums.length; left++) {
    let sum = 0
    for (let right = left; right < nums.length; right++) {
      sum += nums[right]
      if (sum === k) {
        res++
      }
    }
  }

  return res
}
