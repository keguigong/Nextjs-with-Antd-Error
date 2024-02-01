# 3. 无重复字符的最长子串
# https://leetcode.cn/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        lookup = set()
        res = 0
        for i in range(len(s)):
            while s[i] in lookup:
                lookup.remove(s[start])
                start += 1
            else:
                lookup.add(s[i])
                res = max(res, i - start + 1)
        return res
