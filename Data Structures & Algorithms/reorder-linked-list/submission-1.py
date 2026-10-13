# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head: return
        n, node = 1, head
        while node.next:
            node = node.next
            n += 1
        node = head
        half = n // 2
        for i in range(half-1):
            node = node.next
        node_back = node.next
        node.next = None
        prev = None
        while node_back:
            suf = node_back.next
            node_back.next = prev
            prev = node_back
            node_back = suf
        ret = head
        front = head.next
        x = 1
        while prev:
            suf_fore, suf_back = front.next if front else None, prev.next
            if x == 1 or not front:
                ret.next = prev
                prev = suf_back
                x = 0
            else:
                ret.next = front
                front = suf_fore
                x = 1
            ret = ret.next
