# 151. 反转字符串中的单词
# https://leetcode.cn/problems/reverse-words-in-a-string

class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        word = ""
        for index, char in enumerate(s):
            if char != " ":
                word += char
            elif len(word) > 0:
                ans = word + (" " if len(ans) > 0 else "") + ans
                word = ""
            
            if index == len(s) - 1 and len(word) > 0:
                ans = word + (" " if len(ans) > 0 else "") + ans

        return ans