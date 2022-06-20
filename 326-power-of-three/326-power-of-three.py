class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        while True:
            flag = False
            if n % 3 == 0:
                n = n/3
                flag = True
            if flag == False:
                if n == 1:
                    return True
                else:
                    return False