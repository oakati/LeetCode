import math
class Solution(object):
    def isThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        myset = list()
        for i in range(1,n+1):
            if n % i == 0:
                myset.append(i)
        return len(set(myset)) == 3