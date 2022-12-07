/**
 * https://leetcode.cn/problems/longest-substring-without-repeating-characters
 */

function lengthOfLongestSubstring(s: string): number {
  if (s.length === 0) return 0;

  let map = new Map();
  let maxLength = 0;
  let left = 0;

  for (let i = 0; i < s.length; i++) {
    let inChar = s.charAt(i);
    if (map.has(inChar)) {
      left = Math.max(left, map.get(inChar) + 1);
    }
    map.set(inChar, i);
    maxLength = Math.max(maxLength, i - left + 1);
  }

  return maxLength;
}
