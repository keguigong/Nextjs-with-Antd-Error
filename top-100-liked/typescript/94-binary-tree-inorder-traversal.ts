/**
 * 二叉树的中序遍历
 * https://leetcode.cn/problems/binary-tree-inorder-traversal/
 */

export function inorderTraversal(root: TreeNode | null): number[] {
  const res = []

  const inorder = (root: TreeNode) => {
    if (!root) {
      return
    }
    inorder(root.left)
    res.push(root.val)
    inorder(root.right)
  }
  inorder(root)
  return res
}

class TreeNode {
  val: number
  left: TreeNode | null
  right: TreeNode | null
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val
    this.left = left === undefined ? null : left
    this.right = right === undefined ? null : right
  }
}
