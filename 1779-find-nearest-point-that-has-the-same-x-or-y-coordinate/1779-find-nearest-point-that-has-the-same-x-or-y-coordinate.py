class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        index = -1
        dist_record = 0
        
        for i in range(0,len(points)):
            if points[i][0] == x or points[i][1] == y:
                new_dist = abs(points[i][0] - x) + abs(points[i][1] - y)
                if index == - 1 or new_dist < dist_record:
                    index = i
                    dist_record = new_dist
        return index
