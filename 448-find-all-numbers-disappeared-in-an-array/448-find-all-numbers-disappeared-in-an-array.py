class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        myarray = list(range(1,len(nums)+1))
        return set(myarray)-set(nums)
        