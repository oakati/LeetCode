class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n = str(n)
        sum = 0
        for i in n:
            sum += int(i)*int(i)
        if sum == 1 or sum == 7:
            return True
        elif sum < 10:
            return False
        else:
            return self.isHappy(sum)