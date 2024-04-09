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


class Solution1:
    """using dp method"""

    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) < 2:
            return s
        n = len(s)
        left, right, maxLen = 0, 0, 1
        dp = [[False] * n for _ in range(n)]
        for r in range(1, n):
            for l in range(r):
                if s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]):
                    dp[l][r] = True
                    if r - l + 1 > maxLen:
                        maxLen = r - l + 1
                        left = l
                        right = r
        return s[left : right + 1]
