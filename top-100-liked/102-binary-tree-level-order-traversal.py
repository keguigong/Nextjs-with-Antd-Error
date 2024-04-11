# 102. 二叉树的层序遍历
# https://leetcode.cn/problems/binary-tree-level-order-traversal
from collections import deque
from sys import last_exc
from typing import Deque, List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.ans = []

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue: Deque[TreeNode] = deque()
        queue.append(root)
        ans: List[List[int]] = []
        while len(queue):
            n = len(queue)
            layerList = []
            for i in range(n):
                node = queue.popleft()
                layerList.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(layerList)
        return ans

