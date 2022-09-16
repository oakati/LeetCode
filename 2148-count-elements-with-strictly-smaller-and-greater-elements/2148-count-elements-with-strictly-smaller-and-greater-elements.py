class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(set(nums)) <= 2:
            return 0
        return len(nums) - nums.count(min(nums)) - nums.count(max(nums))