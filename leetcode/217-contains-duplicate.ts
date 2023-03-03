/**
 * 存在重复元素
 * https://leetcode.cn/problems/contains-duplicate/
 */

export function containsDuplicate(nums: number[]): boolean {
  let map = new Map<number, boolean>()
  for (let i = 0; i < nums.length; i++) {
    if (!map.has(nums[i])) map.set(nums[i], true)
    else return true
  }
  return false
}
