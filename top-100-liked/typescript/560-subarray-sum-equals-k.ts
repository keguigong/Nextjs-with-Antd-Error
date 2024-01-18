/**
 * 560. 和为 K 的子数组
 * https://leetcode.cn/problems/subarray-sum-equals-k/?envType=study-plan-v2&envId=top-100-liked
 */

export function subarraySum(nums: number[], k: number): number {
  const map = new Map([[0, 1]])
  let preSum = 0
  let count = 0

  for (let i = 0; i < nums.length; i++) {
    preSum += nums[i]

    if (map.has(preSum - k)) {
      count += map.get(preSum - k)
    }

    if (map.has(preSum)) {
      map.set(preSum, map.get(preSum) + 1)
    } else {
      map.set(preSum, 1)
    }
  }

  return count
}
