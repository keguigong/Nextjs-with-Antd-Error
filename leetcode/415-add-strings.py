# 415. 字符串相加
# https://leetcode.cn/problems/add-strings


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        if n > m:
            return self.addStrings(num2, num1)

        ans = ""
        digit = 0
        for i in range(-1, -n - 1, -1):
            sum = int(num1[i]) + int(num2[i]) + digit
            num = sum % 10
            digit = 1 if sum >= 10 else 0
            ans = str(num) + ans

        for j in range(m - n - 1, -1, -1):
            sum = int(num1[j]) + digit
            num = sum % 10
            digit = 1 if sum >= 10 else 0
            ans = str(num) + ans

        if digit > 0:
            ans = "1" + ans

        return ans
