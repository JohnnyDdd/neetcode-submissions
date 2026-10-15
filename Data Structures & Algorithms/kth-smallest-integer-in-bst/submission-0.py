# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root):
            visited = []
            if root.left and root.left.val not in visited: 
                visited += (dfs(root.left))
            visited.append(root.val)
            if root.right and root.right.val not in visited:
                visited += (dfs(root.right))
            return visited
        list_examine = dfs(root)
        return list_examine[k-1] if list_examine else None