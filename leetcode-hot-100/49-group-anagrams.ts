/**
 * 49. 字母异位词分组
 * https://leetcode.cn/problems/group-anagrams/
 */
export function groupAnagrams(strs: string[]): string[][] {
  const map = new Map<string, Array<string>>()

  for (let i = 0; i < strs.length; i++) {
    const sortedStr = Array.from(strs[i]).sort().join("")
    if (map.has(sortedStr)) {
      map.get(sortedStr).push(strs[i])
    } else {
      map.set(sortedStr, [strs[i]])
    }
  }

  return Array.from(map.values())
}

let strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
console.log(groupAnagrams(strs))
