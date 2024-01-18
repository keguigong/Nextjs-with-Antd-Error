/**
 * 128. 最长连续序列
 * https://leetcode.cn/problems/longest-consecutive-sequence/
 */

export function longestConsecutive(nums: number[]): number {
  let numSet: Set<number> = new Set()
  for (let i = 0; i < nums.length; i++) {
    numSet.add(nums[i])
  }

  let longestStreak = 0

  for (const num of numSet) {
    if (!numSet.has(num - 1)) {
      let currentNum = num
      let currentStreak = 1

      while (numSet.has(currentNum + 1)) {
        currentNum += 1
        currentStreak += 1
      }

      longestStreak = Math.max(longestStreak, currentStreak)
    }
  }

  return longestStreak
}
