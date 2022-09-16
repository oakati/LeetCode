import numpy as np
class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return np.sort(np.square(np.array(nums)))
        