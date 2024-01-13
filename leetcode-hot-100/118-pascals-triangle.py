"""
118. 杨辉三角
https://leetcode.cn/problems/pascals-triangle/
"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1] * i for i in range(1, numRows + 1)]
        if numRows <= 2:
            return ans
        for i in range(1, numRows):
            for j in range(1, i):
                ans[i][j] = ans[i - 1][j - 1] + ans[i - 1][j]
        return ans


print(Solution().generate(4))
