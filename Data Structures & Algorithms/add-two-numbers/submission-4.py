# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = l1, l2
        
        ret = None
        traverse = ret
        carryover = 0
        while n1 or n2 or carryover > 0:
            d1, d2 = 0,0
            if n1: d1 = n1.val
            if n2: d2 = n2.val
            dsum = d1 + d2 + carryover
            if dsum >= 10:
                carryover = 1
                dsum -= 10
            else: carryover = 0
            node = ListNode(dsum)
            if not ret: 
                ret = node
            else:
                traverse.next = node
            traverse = node
            n1 = n1.next if n1 else None
            n2 = n2.next if n2 else None
        return ret