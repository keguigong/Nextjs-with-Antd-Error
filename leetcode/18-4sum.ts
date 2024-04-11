/**
 * 四数之和
 * https://leetcode.cn/problems/4sum/
 */

export function fourSum(nums: number[], target: number): number[][] {
  let result: number[][] = []
  const len = nums.length
  if (nums == null || len < 4) return result
  nums.sort((a, b) => a - b)

  for (let i = 0; i < len - 3; i++) {
    if (i > 0 && nums[i] === nums[i - 1]) continue
    if (nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target) break
    if (nums[i] + nums[len - 3] + nums[len - 2] + nums[len - 1] < target) continue

    for (let j = i + 1; j < len - 2; j++) {
      if (j > i + 1 && nums[j] === nums[j - 1]) continue
      if (nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target) break
      if (nums[i] + nums[j] + nums[len - 2] + nums[len - 1] < target) continue

      let left = j + 1,
        right = len - 1
      while (left < right) {
        const sum = nums[i] + nums[j] + nums[left] + nums[right]
        if (sum === target) {
          result.push([nums[i], nums[j], nums[left], nums[right]])
          while (left < right && nums[left] === nums[left + 1]) left++
          while (left < right && nums[right] === nums[right - 1]) right--
          left++
          right--
        } else if (sum < target) {
          left++
        } else {
          right--
        }
      }
    }
  }

  return result
}

let nums = [-1, 0, 1, 2, -1, -4]
let target = 5
console.log(fourSum(nums, target))
