"""
20. 有效的括号
https://leetcode.cn/problems/valid-parentheses/
"""


class Solution:
    def isValid(self, s: str) -> bool:
        dic = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for symbol in s:
            if symbol in dic:
                stack.append(symbol)
            elif stack == [] or symbol != dic[stack.pop()]:
                return False
        return stack == []
