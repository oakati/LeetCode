import numpy as np
class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        arr = np.array(grid)
        return np.count_nonzero(arr) + np.sum(np.amax(arr, axis=1)) + np.sum(np.amax(arr, axis=0))