# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder: return None
        if len(preorder) == 1: return TreeNode(preorder[0])
        in_idx = {val:idx for idx,val in enumerate(inorder)}
        def recur(pl, pr, il, ir):
            #print(pl,pr,il,ir)
            if pl == pr or il == ir: return None
            node = TreeNode(preorder[pl])
            i = in_idx[node.val]
            node.left = recur(pl+1, pl+1-i+il, il, i)
            node.right = recur(pl+i-il+1, pr, i+1, ir)
            return node
        ret = recur(0, len(preorder), 0, len(inorder))
        return ret