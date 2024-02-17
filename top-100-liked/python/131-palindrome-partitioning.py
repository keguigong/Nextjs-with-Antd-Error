# 131. 分割回文串
# https://leetcode.cn/problems/palindrome-partitioning

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def dfs(i, comb):
            if i == len(s):
                ans.append(comb[:])
                return
            
            for j in range(i, len(s)):
                if isPalindrome(i, j):
                    dfs(j + 1, comb + [s[i : j + 1]])
        
        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        dfs(0, [])
        return ans