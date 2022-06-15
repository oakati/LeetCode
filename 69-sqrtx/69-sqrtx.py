class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i = 0
        while True:
            square = i*i
            if square > x:
                return (i - 1)
            i = i + 1