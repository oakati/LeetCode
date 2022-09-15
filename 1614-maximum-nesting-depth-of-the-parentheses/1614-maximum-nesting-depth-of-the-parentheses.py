class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        depth = 0
        record = 0
        for i in s:
            if i == "(":
                depth = depth + 1
                record = max(record, depth)
            elif i == ")":
                depth = depth - 1
        return record