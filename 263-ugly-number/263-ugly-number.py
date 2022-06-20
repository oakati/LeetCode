class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False
        while True:
            flag = 0
            if n % 2 == 0:
                n = n/2
                flag = True
            if n % 3 == 0:
                n = n/3
                flag = True
            if n % 5 == 0:
                n = n/5
                flag = True
            if flag == False:
                if n == 1:
                    return True
                else:
                    return False
            