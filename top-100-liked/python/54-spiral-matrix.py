# 54. 螺旋矩阵
# https://leetcode.cn/problems/spiral-matrix
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        direction = "right"
        left, top, right, bottom = 0, 0, len(matrix[0]) - 1, len(matrix) - 1
        while left <= right and top <= bottom:
            # print("left = {}, top = {}, right = {}, bottom = {}".format(left, top, right, bottom))
            # print("ans = {}".format(ans))
            if len(ans) == len(matrix[0] * len(matrix)):
                break
            if direction == "right":
                for i in range(left, right + 1):
                    ans.append(matrix[top][i])
                top += 1
                direction = "bottom"
                continue
            if direction == "bottom":
                for i in range(top, bottom + 1):
                    ans.append(matrix[i][right])
                right -= 1
                direction = "left"
                continue
            if direction == "left":
                for i in range(right, left - 1, -1):
                    ans.append(matrix[bottom][i])
                bottom -= 1
                direction = "top"
                continue
            if direction == "top":
                for i in range(bottom, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1
                direction = "right"
                continue
        return ans
