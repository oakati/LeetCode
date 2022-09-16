# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def myfunc(root, counter):
            if root != None:
                counter = counter + 1
                if root.left != None and root.right != None:
                    counter = max(myfunc(root.left, counter), myfunc(root.right, counter))
                elif root.left == None and root.right != None:
                    counter = myfunc(root.right, counter)
                elif root.left != None and root.right == None:
                    counter = myfunc(root.left, counter)
            return counter
            
        counter = 0
        return myfunc(root, counter)