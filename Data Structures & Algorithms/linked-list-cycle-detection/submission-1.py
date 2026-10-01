# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        index_head = head
        slow_node = head
        fast_node = head
        while slow_node and fast_node:
            slow_node = slow_node.next if slow_node else None
            fast_node = fast_node.next.next if fast_node.next else None
            if slow_node == fast_node and slow_node and fast_node: return True
        return False