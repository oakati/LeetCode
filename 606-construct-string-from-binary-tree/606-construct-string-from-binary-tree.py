# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def tree2str(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        def func(root,out):
            if root != None:
                out += str(root.val)
            if root.left != None:
                out += "("
                out = func(root.left,out)
                out += ")"                
            if root.right != None:
                if root.left == None:
                    out += "("
                    out += ")"
                out += "("
                out = func(root.right,out)
                out += ")"
            return out
    
        out = ""
        out = func(root,out)
        return out