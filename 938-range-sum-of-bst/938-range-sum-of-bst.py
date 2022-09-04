# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        if root != None and root.val >= low and root.val <= high:
            count1 = root.val
        else:
            count1 = 0
        if root.left != None:
            count2 = self.rangeSumBST(root.left, low, high)
        else:
            count2 = 0
        if root.right != None:
            count3 = self.rangeSumBST(root.right, low, high)
        else:
            count3 = 0        
        return count1 + count2 + count3