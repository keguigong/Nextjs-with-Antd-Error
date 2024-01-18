# 543. 二叉树的直径
# https://leetcode.cn/problems/diameter-of-binary-tree/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.ans

    def dfs(self, root: Optional[TreeNode]):
        if not root:
            return 0
        else:
            left = self.dfs(root.left)
            right = self.dfs(root.right)
            self.ans = max(self.ans, left + right)
            return max(left, right) + 1
