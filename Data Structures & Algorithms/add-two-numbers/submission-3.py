# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = l1, l2
        str_1,str_2 = '',''
        list_nodes = []
        while n1:
            str_1 += str(n1.val)
            n1 = n1.next
        while n2:
            str_2 += str(n2.val)
            n2 = n2.next

        int_1 = int(str_1[::-1])
        int_2 = int(str_2[::-1])
        
        sum = (list(str(int_1+int_2)))[::-1]
        for digit in sum:
            list_nodes.append(ListNode(int(digit)))
        for i in range(len(list_nodes)):
            if i == len(list_nodes)-1: list_nodes[i].next = None
            else: list_nodes[i].next = list_nodes[i+1]
        return list_nodes[0]
        