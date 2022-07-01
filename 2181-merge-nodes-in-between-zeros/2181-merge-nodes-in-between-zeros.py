# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        mylist = ListNode()
        mylist2 = mylist
        counter = 0
        while head != None:
            if head.val != 0:
                counter = counter + head.val
            elif head.val == 0 and counter != 0:
                mylist2.val = counter
                counter = 0
                if head.next != None:
                    mylist2.next = ListNode()
                    mylist2 = mylist2.next
            head = head.next

            
        return mylist