/**
 * 删除并获得点数
 * https://leetcode.cn/problems/delete-and-earn/
 */

export function deleteAndEarn(nums: number[]): number {
  let maxVal = 0
  for (const val of nums) {
    maxVal = Math.max(maxVal, val)
  }
  const sum = new Array(maxVal + 1).fill(0)
  for (const val of nums) {
    sum[val] += val
  }
  return rob(sum)
}

function rob(nums: number[]): number {
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

const nums = [3, 4, 2]
console.log(deleteAndEarn(nums))
