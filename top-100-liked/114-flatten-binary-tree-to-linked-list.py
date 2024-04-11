# 114. 二叉树展开为链表
# https://leetcode.cn/problems/flatten-binary-tree-to-linked-list/

# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def helper(root: TreeNode, queue: List[TreeNode]):
    queue.append(root)
    if root.left:
        helper(root.left, queue)
    if root.right:
        helper(root.right, queue)


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        dummy = TreeNode(0, None, None)
        p = dummy
        queue = []
        helper(root, queue)
        for node in queue:
            p.right = node
            p = p.right
            p.left = None

        return dummy.right
