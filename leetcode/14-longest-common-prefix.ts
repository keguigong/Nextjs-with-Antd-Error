/**
 * 最长公共前缀
 * https://leetcode.cn/problems/longest-common-prefix/
 */

function longestCommonPrefix(strs: string[]): string {
  let prefix = strs[0];

  for (let i = 0; i < strs.length; i++) {
    prefix = getCommonPrefix(prefix, strs[i]);
  }
  return prefix;
}

function getCommonPrefix(str1: string, str2: string): string {
  let len = Math.min(str1.length, str2.length);
  let commonStr = "";
  let index = 0;
  while (index < len) {
    if (str1[index] === str2[index]) {
      commonStr += str1[index];
      index++;
    } else break;
  }
  return commonStr;
}
