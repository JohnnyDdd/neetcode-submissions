# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        total = 0
        ret = -1
        def dfs(root):
            nonlocal total, ret
            if ret == -1:
                if root.left: 
                    dfs(root.left) 
                total += 1
                if total == k: 
                    ret = root.val
                    return
                if root.right:
                    dfs(root.right)
        dfs(root)
        return ret