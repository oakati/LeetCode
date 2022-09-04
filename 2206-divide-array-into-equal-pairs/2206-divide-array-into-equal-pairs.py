class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        flag = True
        for i in set(nums):
            if nums.count(i) % 2 == 1:
                flag = False
        return flag