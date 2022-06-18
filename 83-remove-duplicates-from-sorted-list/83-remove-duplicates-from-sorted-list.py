# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        def myfunc(head):
            
            if head != None and head.next != None:
                if head.val == head.next.val:
                    if head.next.next != None:
                        head.next = head.next.next
                        a=myfunc(head)
                    else:
                        head.next = None
                else:
                    a=myfunc(head.next)
                
            return head
        
        return myfunc(head)