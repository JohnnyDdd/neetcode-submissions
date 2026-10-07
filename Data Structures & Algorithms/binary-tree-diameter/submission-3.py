# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getHeight(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right))

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        ret = 0
        if root.left: ret += self.getHeight(root.left)
        if root.right: ret += self.getHeight(root.right)
        ret = max(ret, self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
        return ret

