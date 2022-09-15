import math
class Solution(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [0]*(n+1)
        if n >= 1:
            nums[1] = 1
        for i in range(2,n+1):
            if i % 2 == 0:
                nums[i] = nums[i/2]
            else:
                nums[i] = nums[int(math.floor(i/2))] + nums[int(math.floor(i/2)+1)]
        return max(nums)
            