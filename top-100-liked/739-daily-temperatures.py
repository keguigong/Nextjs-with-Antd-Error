# 739. 每日温度
# https://leetcode.cn/problems/daily-temperatures
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        ans = [0] * n

        for i in range(n):
            while len(stack) and temperatures[i] > temperatures[stack[-1]]:
                small_i = stack.pop()
                ans[small_i] = i - small_i
            stack.append(i)

        return ans
