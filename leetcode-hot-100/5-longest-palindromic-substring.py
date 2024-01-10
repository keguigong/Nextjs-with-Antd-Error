# 5. 最长回文子串
# https://leetcode.cn/problems/longest-palindromic-substring/


class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            left, right = i, i
            while right + 1 < len(s) and s[right + 1] == s[left]:
                right += 1
            while left - 1 >= 0 and right + 1 < len(s) and s[left - 1] == s[right + 1]:
                left -= 1
                right += 1
            if right > left and len(ans) < right - left + 1:
                ans = s[left : right + 1]

        return ans if ans else s[0]
