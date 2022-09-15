# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        m_head = head
        i = 0
        while head != None:
            i = i + 1
            head = head.next
        val = i/2
        i = 0
        while i < val:
            m_head = m_head.next
            i = i +1
        return m_head
