import numpy as np
class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        record = 0
        for i in range(0, len(points)-2):
            for j in range(1, len(points)-1):
                for k in range(2, len(points)):
                    m_arr = [[points[i][0], points[i][1], 1], [points[j][0], points[j][1], 1], [points[k][0], points[k][1], 1]]
                    m_arr = np.array(m_arr)
                    record = max(record, abs(np.linalg.det(m_arr)))
        return record/2