# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = 0
        cur = head
        while cur:
            i += 1
            cur = cur.next
        if i == 1: return None
        elif i == n: return head.next
        else: 
            t = i - n
            cur = head
            j = 1
            while j < t:
                cur = cur.next
                j += 1
            cur.next = cur.next.next if cur.next.next else None
        return head
             
        
