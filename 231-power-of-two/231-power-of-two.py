class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        while True:
            flag = False
            if n % 2 == 0:
                n = n/2
                flag = True
            if flag == False:
                if n == 1:
                    return True
                else:
                    return False