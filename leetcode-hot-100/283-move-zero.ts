/**
 * 283. 移动零
 * https://leetcode.cn/problems/move-zeroes
 */

export function moveZeroes(nums: number[]): void {
  let j = 0
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] != 0) {
      let temp = nums[i]
      nums[i] = nums[j]
      nums[j] = temp
      j += 1
    }
  }
}
