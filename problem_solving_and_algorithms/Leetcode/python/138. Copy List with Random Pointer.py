"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        
        current = head
        
        while current:
            copied = Node(current.val)
            copied.next = current.next
            current.next = copied
            current = copied.next

        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next

        dummy = Node(0)
        copied_current, current = dummy, head
        
        while current:
            copied_current.next = current.next
            current.next = current.next.next
            copied_current, current = copied_current.next, current.next
            
        return dummy.next

    
