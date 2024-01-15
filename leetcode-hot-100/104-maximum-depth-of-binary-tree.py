# 104. 二叉树的最大深度
# https://leetcode.cn/problems/maximum-depth-of-binary-tree
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def countDepth(root: Optional[TreeNode], count=0) -> int:
    if not root:
        return count
    else:
        return max(countDepth(root.left, count + 1), countDepth(root.right, count + 1))


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return countDepth(root, 0)
