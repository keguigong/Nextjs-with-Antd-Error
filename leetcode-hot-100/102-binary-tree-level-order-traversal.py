# 102. 二叉树的层序遍历
# https://leetcode.cn/problems/binary-tree-level-order-traversal
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.ans = []

    def printLevel(self, queue: List[TreeNode]):
        temp: List[TreeNode] = []
        ans: List[int] = []
        for node in queue:
            ans.append(node.val)
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
        self.ans.append(ans)
        if len(temp) > 0:
            self.printLevel(temp)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue: List[TreeNode] = []
        if not root:
            return []
        else:
            queue.append(root)
        self.printLevel(queue)
        return self.ans
