# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root, root.val)]
        ret = 1
        while stack:
            cur, cur_max = stack.pop()
            if cur.left:
                if cur.left.val >= cur_max: ret += 1 
                stack.append((cur.left, max(cur_max, cur.left.val)))
            if cur.right:
                if cur.right.val >= cur_max: ret += 1 
                stack.append((cur.right, max(cur_max, cur.right.val)))
        return ret