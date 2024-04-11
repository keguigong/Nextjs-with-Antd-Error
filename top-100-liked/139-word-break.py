# 139. 单词拆分
# https://leetcode.cn/problems/word-break/

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        s_length = len(s)
        dp = [True] + s_length * [False]
        for i in range(1, s_length + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]
