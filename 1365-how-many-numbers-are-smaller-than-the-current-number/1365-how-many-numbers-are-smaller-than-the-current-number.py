class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        mylist = []
        for i in range(0,len(nums)):
            counter = 0
            for j in range(0,len(nums)):
                if j != i and nums[j] < nums[i]:
                    counter = counter + 1
            mylist.append(counter)
        return mylist