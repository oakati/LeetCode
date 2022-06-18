class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        counter = 0
        a = len(nums)
        while True:
            if val in nums:
                nums.remove(val)
                counter = counter + 1
            else:
                break
        return a-counter