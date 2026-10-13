"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None

        node = head
        node_list = []
        node_dict = {}

        while node:
            copy = Node(node.val)
            node_dict[node] = copy
            node_list.append(copy)
            node = node.next
        
        for i in range(len(node_list)):
            if i == len(node_list)-1: node_list[i].next = None
            else: node_list[i].next = node_list[i+1]
        
        for key in node_dict:
            node_dict[key].random = node_dict[key.random] if key.random else None

        return node_list[0]





