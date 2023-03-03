/**
 * 找出字符串中第一个匹配项的下标
 * https://leetcode.cn/problems/find-the-index-of-the-first-occurrence-in-a-string/
 */

export function strStr(haystack: string, needle: string): number {
  const len = haystack.length - needle.length
  if (len < 0) return -1

  let needleIndex = 0
  for (let i = 0; i < haystack.length; i++) {
    let hayIndex = i
    if (haystack[hayIndex] !== needle[needleIndex]) continue

    while (needleIndex < needle.length && haystack[hayIndex] === needle[needleIndex]) {
      hayIndex++
      needleIndex++
    }

    if (needleIndex === needle.length) {
      return hayIndex - needleIndex
    } else {
      needleIndex = 0
    }
  }

  return -1
}

const haystack = "mississippi"
const needle = "issip"
console.log(strStr(haystack, needle))
