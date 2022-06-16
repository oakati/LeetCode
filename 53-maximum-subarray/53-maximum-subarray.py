class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        record = nums[0]
        current_sum = nums[0]
        for i in nums[1:]:
            current_sum += i
            if current_sum < i:
                current_sum = i
            if current_sum > record:
                record = current_sum
        return record
                    