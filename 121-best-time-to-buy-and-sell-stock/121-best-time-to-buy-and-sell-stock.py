class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        left = len(prices)-2
        right = len(prices)-1
        val = 0
        while left >= 0:
            mydifference = prices[right]-prices[left]
            if mydifference > 0:
                if mydifference > val:
                    val = prices[right]-prices[left]
            else:
                right=left
            left -= 1
        return val