# 236. 二叉树的最近公共祖先
# https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.ans: "TreeNode"

    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        def helper(root):
            count = 0
            if root:
                if root.val == p.val or root.val == q.val:
                    count += 1
                if helper(root.left):
                    count += 1
                if helper(root.right):
                    count += 1
                if count >= 2:
                    self.ans = root

            return True if count > 0 else False

        helper(root)
        return self.ans
