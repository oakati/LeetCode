class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        val = num % 3
        if val == 0:
            val2 = num/3
            return [val2-1,val2,val2+1]
        else:
            return []
        