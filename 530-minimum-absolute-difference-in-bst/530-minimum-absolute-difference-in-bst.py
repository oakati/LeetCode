# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        mylist = []
        mylist.append(root.val)
        def func(node,mylist):
            if node.left != None:
                mylist.append(node.left.val)
                func(node.left,mylist)  
            if node.right != None:
                mylist.append(node.right.val)
                func(node.right,mylist)
        func(root,mylist)
        mylist.sort()
        record = max(mylist)
        for i in range(len(mylist)-1):
            if mylist[i+1]-mylist[i]<record:
                record = mylist[i+1]-mylist[i]
        return record