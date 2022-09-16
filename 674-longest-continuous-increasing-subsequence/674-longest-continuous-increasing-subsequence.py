class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 1
        counter = 1
        record = 1
        for i in range(0, len(nums)-1):
            if nums[i+1] > nums[i]:
                counter = counter + 1
                record = max(record, counter)
            else:
                counter = 1
        return record