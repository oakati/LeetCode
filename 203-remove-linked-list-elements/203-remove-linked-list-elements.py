# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head != None:
            if head.val != val:
                break
            head = head.next
        save_head = head
        
        while head != None and head.next != None:
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next
        return save_head