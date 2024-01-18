# 144. 二叉树的前序遍历
# https://leetcode.cn/problems/binary-tree-preorder-traversal
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.ans: List[int] = []

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return self.ans
        else:
            self.ans.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
            return self.ans
