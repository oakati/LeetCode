from math import factorial as fct
class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        myset = set(nums)
        for i in myset:
            temp = nums.count(i)
            if temp >= 2:
                counter = counter + fct(temp)/(fct(2)*fct(temp-2)) 
        return counter