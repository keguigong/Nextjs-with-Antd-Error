# 79. 单词搜索
# https://leetcode.cn/problems/word-search
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def helper(visited: List[List[bool]], row: int, col: int, index: int) -> bool:
            nonlocal board, word, rows, cols
            if (
                row >= 0
                and col >= 0
                and row < rows
                and col < cols
                and not visited[row][col]
                and board[row][col] == word[index]
            ):
                # print("row = {}, col = {}, char = {}".format(row, col, word[index]))
                if index < len(word) - 1:
                    visited[row][col] = True
                    if (
                        helper(visited, row + 1, col, index + 1)
                        or helper(visited, row - 1, col, index + 1)
                        or helper(visited, row, col + 1, index + 1)
                        or helper(visited, row, col - 1, index + 1)
                    ):
                        return True
                    else:
                        """Important! Remember to reset visited state if none matches"""
                        visited[row][col] = False
                else:
                    return True

            return False

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    visited = [[False for _ in range(cols)] for _ in range(rows)]
                    if helper(visited, row, col, 0):
                        return True

        return False
