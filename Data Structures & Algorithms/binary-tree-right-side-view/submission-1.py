# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root])
        lv_size = 1
        lv_list = []
        ret = []
        while queue:
            for i in range(lv_size):
                cur = queue.popleft()
                if not cur: break
                lv_list.append(cur.val)
                if cur.left:    queue.append(cur.left)
                if cur.right:   queue.append(cur.right)
            lv_size = len(queue)
            if not lv_list: break
            ret.append(lv_list.pop())
            lv_list = []
        return ret