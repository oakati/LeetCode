class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        myset = set(nums)
        mylist = list(myset)
        mylist.sort()
        for i in range(len(mylist)):
            nums[i] = mylist[i]
        print(nums)
        print(mylist)
            
        return len(mylist)
