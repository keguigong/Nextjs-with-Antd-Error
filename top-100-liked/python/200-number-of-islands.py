# 200. 岛屿数量
# https://leetcode.cn/problems/number-of-islands
from pickletools import read_string1
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        m, n = len(grid[0]), len(grid)
        visited: List[List[bool]] = [[False] * m for _ in range(n + 1)]

        def dfs(col: int, row: int, ex_source=""):
            if (
                col >= 0
                and col < m
                and row >= 0
                and row < n
                and grid[row][col] == "1"
                and not visited[row][col]
            ):
                visited[row][col] = True
                if ex_source != "right":
                    dfs(col + 1, row, "left")
                if ex_source != "bottom":
                    dfs(col, row + 1, "top")
                if ex_source != "left":
                    dfs(col - 1, row, "right")
                if ex_source != "up":
                    dfs(col, row - 1, "bottom")

        for row in range(n):
            for col in range(m):
                if grid[row][col] == "1" and not visited[row][col]:
                    count += 1
                    dfs(col, row)
        return count
