class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        L = ceil(sqrt(area))
        
        while True:
            if area % L != 0:
                L = L + 1
            else:
                break
        return [int(L), int(area/L)]