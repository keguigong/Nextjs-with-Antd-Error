# 94. 二叉树的中序遍历
# https://leetcode.cn/problems/binary-tree-inorder-traversal
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

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return self.ans
        else:
            self.inorderTraversal(root.left)
            self.ans.append(root.val)
            self.inorderTraversal(root.right)
            return self.ans
