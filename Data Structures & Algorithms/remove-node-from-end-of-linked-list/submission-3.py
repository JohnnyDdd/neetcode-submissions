# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        list_nodes = []
        while cur:
            list_nodes.append(cur)
            cur = cur.next
        ln = len(list_nodes)
        if ln == 1: return None
        else:
            if n == ln:
                print('1st node')
                return list_nodes[1]
            if n == 1:
                print('last node')
                list_nodes[-n-1].next = None
            else:
                node_bef = list_nodes[-n-1]
                node_aft = list_nodes[-n+1]
                node_bef.next = node_aft
        return head
