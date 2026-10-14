# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []
        queue = deque([root])
        lv_list = []
        lv_size = len(queue)
        while queue:
            for i in range(lv_size):
                cur = queue.popleft()
                if not cur: break
                lv_list.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            if lv_list: ret.append(lv_list)
            lv_size = len(queue)
            lv_list = []
        return ret