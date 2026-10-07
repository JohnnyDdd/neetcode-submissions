# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]

        ret = False
        def sameTree(r):
            stack = [(r,subRoot)]
            while stack:
                c, sc = stack.pop()
                if not c and not sc: continue
                if (c and not sc) or (not c and sc): return False 
                if c.val != sc.val: return False
                else:
                    stack.append((c.left if c.left else None, sc.left if sc.left else None))
                    stack.append((c.right if c.right else None, sc.right if sc.right else None))
            return True
            
        while stack:
            c = stack.pop()
            if not c: continue
            if c.val == subRoot.val:  
                ret = ret or sameTree(c)
                if ret: return ret
            if c.left: stack.append(c.left)
            if c.right: stack.append(c.right)
        return ret
