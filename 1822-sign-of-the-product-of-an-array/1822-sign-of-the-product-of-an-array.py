class Solution(object):
    def arraySign(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if 0 in nums:
            return 0
        negatives = [i > 0 for i in nums]
        if negatives.count(False)%2 == 0:
            return 1
        else:
            return -1
        