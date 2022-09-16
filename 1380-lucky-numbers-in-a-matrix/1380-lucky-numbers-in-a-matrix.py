import numpy as np
class Solution(object):
    def luckyNumbers (self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        matrix = np.array(matrix)
        return np.intersect1d(np.min(matrix, axis=1), np.max(matrix, axis=0))