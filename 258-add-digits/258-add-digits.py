class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while(num >= 10):
            ans = 0
            num = str(num)
            for i in num:
                ans += int(i)
            num = ans
        return num