# 73. 矩阵置零
# https://leetcode.cn/problems/set-matrix-zeroes/
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, col = len(matrix), len(matrix[0])
        row0_flag, col0_flag = False, False

        for j in range(col):
            if matrix[0][j] == 0:
                row0_flag = True

        for i in range(row):
            if matrix[i][0] == 0:
                col0_flag = True
                break

        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0

        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if row0_flag:
            for j in range(col):
                matrix[0][j] = 0

        if col0_flag:
            for i in range(row):
                matrix[i][0] = 0
