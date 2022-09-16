import numpy as np
class Solution(object):
    def minStartValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = np.array(nums)
        a = np.min(nums.cumsum())
        if a < 0:
            return 1 - a
        else:
            return 1