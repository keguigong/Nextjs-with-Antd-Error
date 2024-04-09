# 14. 最长公共前缀
# https://leetcode.cn/problems/longest-common-prefix


from typing import List


def getCommonPrefixOfTwo(str1: str, str2: str):
    i = 0
    while i < min(len(str1), len(str2)) and str1[i] == str2[i]:
        i += 1
    return str1[:i]


def getCommonPrefix(strs: List[str], left: int, right: int):
    if left == right:
        return strs[left]
    elif right - left + 1 == 2:
        return getCommonPrefixOfTwo(strs[left], strs[right])
    else:
        mid = (right - left) // 2 + left
        str1 = getCommonPrefix(strs, left, mid)
        str2 = getCommonPrefix(strs, mid + 1, right)
        return getCommonPrefixOfTwo(str1, str2)


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not len(strs):
            return ""
        return getCommonPrefix(strs, 0, len(strs) - 1)
