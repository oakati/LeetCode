class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n = bin(n)[2:]
        flag = True
        for i in range(0, len(n)-1):
            if n[i] == n[i+1]:
                flag = False
                break
        return flag
            