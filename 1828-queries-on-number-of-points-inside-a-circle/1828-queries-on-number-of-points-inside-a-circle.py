class Solution(object):
    def countPoints(self, points, queries):
        """
        :type points: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        mylist = []
        for i in queries:
            counter = 0
            for j in points:
                if pow((i[0]-j[0]),2) + pow((i[1]-j[1]),2) <= pow((i[2]),2):
                    counter = counter + 1
            mylist.append(counter)
        return mylist