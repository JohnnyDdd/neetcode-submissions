# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        elif not list2: return list1
        elif (not list1) and (not list2): return None

        node1 = list1
        node2 = list2
        node = ListNode(0,None)
        head = None
        iterator = None

        while node1 or node2:
            rest1 = node1.next if node1 else None
            rest2 = node2.next if node2 else None
            if not head:
                print("initialize")
                if node1.val <= node2.val:
                    head = node1
                    node1 = rest1
                elif node2.val < node1.val:
                    head = node2
                    node2 = rest2
                iterator = head
            if not node1: 
                print("list 2 left")
                iterator.next = node2
                node2 = rest2
            elif not node2:
                print("list 1 left")
                iterator.next = node1
                node1 = rest1
            else:
                print("Comparing")
                if node2.val <= node1.val:
                    iterator.next = node2
                    node2 = rest2
                else: 
                    iterator.next = node1
                    node1 = rest1
            iterator = iterator.next if iterator.next else iterator
        return head


