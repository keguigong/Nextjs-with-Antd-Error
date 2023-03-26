/**
 * 在排序数组中查找元素的第一个和最后一个位置
 * https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/
 */

function binarySearch(nums: number[], target: number, lower: boolean) {
  let l = 0,
    r = nums.length,
    ans = nums.length
  while (l <= r) {
    const mid = Math.floor((l + r) / 2)
    if (nums[mid] > target || (lower && nums[mid] >= target)) {
      r = mid - 1
      ans = mid
    } else {
      l = mid + 1
    }
  }
  return ans
}

export function searchRange(nums: number[], target: number): number[] {
  let ans = [-1, -1]
  const l = binarySearch(nums, target, true)
  const r = binarySearch(nums, target, false) - 1
  if (l <= r && r < nums.length && nums[l] === target && nums[r] === target) {
    ans = [l, r]
  }
  return ans
}

let nums = [5, 7, 7, 8, 8, 10]
let target = 8
console.log(searchRange(nums, target))
