# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        visited_p = []
        visited_q = []
        
        stack = [(p,q)]
        while stack:
            cp, cq = stack.pop()
            if not cp and not cq: continue
            if not cp and cq: return False
            if not cq and cp: return False
            if cp.val != cq.val: return False

            visited_p.append(cp.val)
            visited_q.append(cq.val)

            stack.append((cp.left if cp.left else None, cq.left if cq.left else None))
            stack.append((cp.right if cp.right else None, cq.right if cq.right else None))

        print(visited_p, visited_q)
        return visited_p == visited_q