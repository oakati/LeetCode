# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        a = head
        b = head
        while b and b.next:
            a = a.next
            b = b.next.next
            if a == b:
                return True
        return False