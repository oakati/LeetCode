# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        a = head
        mylist = []
        while a and a.next:
            mylist.append(a)
            a = a.next
            for i in mylist:
                if i == a:
                    return i
        return
        