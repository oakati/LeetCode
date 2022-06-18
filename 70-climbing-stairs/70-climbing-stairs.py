from math import factorial as fct
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ones = n % 2
        counter = 0
        for twos in range(int(floor(n/2)),-1,-1):
            counter = counter + fct(twos+ones)/(fct(twos)*fct(ones))
            ones = ones + 2
        return counter
            