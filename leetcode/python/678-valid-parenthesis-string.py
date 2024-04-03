# 678. 有效的括号字符串
# https://leetcode.cn/problems/valid-parenthesis-string


class Solution:
    def checkValidString(self, s: str) -> bool:
        leftStack = []
        starStack = []
        n = len(s)
        for i in range(n):
            char = s[i]
            if char == "(":
                leftStack.append(i)
            elif char == "*":
                starStack.append(i)
            else:
                if len(leftStack):
                    leftStack.pop()
                elif len(starStack):
                    starStack.pop()
                else:
                    return False

        while len(leftStack) and len(starStack):
            left = leftStack.pop()
            star = starStack.pop()
            if left > star:
                return False

        return len(leftStack) == 0
