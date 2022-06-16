class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        for i in range(len(nums)):
            if len(nums) == 1:
                return nums[0]
            elif i == 0 and nums[i] != nums[i+1]:
                return nums[i]
            elif i == len(nums)-1 and nums[i] != nums[i-1]:
                return nums[i]
            elif i == 0 or i == len(nums)-1:
                continue
            if nums[i-1] != nums[i] and nums[i] != nums[i+1]:
                return nums[i]
        