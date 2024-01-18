# 145. 二叉树的后序遍历
# https://leetcode.cn/problems/binary-tree-postorder-traversal
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

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return self.ans
        else:
            self.postorderTraversal(root.left)
            self.postorderTraversal(root.right)
            self.ans.append(root.val)
            return self.ans
