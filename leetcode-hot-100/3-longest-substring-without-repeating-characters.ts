/**
 * 3. 无重复字符的最长子串
 * https://leetcode.cn/problems/longest-substring-without-repeating-characters/
 */

export function lengthOfLongestSubstring(s: string): number {
  if (!s) return 0
  let left = 0
  const lookup: Set<string> = new Set()
  let maxLen = 0
  let currLen = 0

  for (let i = 0; i < s.length; i++) {
    currLen += 1
    while (lookup.has(s[i])) {
      lookup.delete(s[left])
      left += 1
      currLen -= 1
    }
    maxLen = Math.max(maxLen, currLen)
    lookup.add(s[i])
  }

  return maxLen
}
