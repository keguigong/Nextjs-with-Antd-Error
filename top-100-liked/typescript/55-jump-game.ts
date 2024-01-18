/**
 * 跳跃游戏
 * https://leetcode.cn/problems/jump-game/
 */

export function canJump(nums: number[]): boolean {
  const n = nums.length
  let rightMost = 0
  for (let i = 0; i < n; i++) {
    if (i <= rightMost) {
      rightMost = Math.max(rightMost, i + nums[i])
      if (rightMost >= n - 1) {
        return true
      }
    }
  }
  return false
}

const nums = [2, 3, 1, 1, 4]
console.log(canJump(nums))
