class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prevleft=0
        prevright=sum(nums)-nums[0]
        curleft=0
        curright=sum(nums)-nums[0]
        
        if curleft == curright:
            return 0
        for i in range(1,len(nums)):
            prevleft=curleft
            prevright=curright
            curleft += nums[i-1]
            curright -=nums[i]
            if curleft == curright:
                return i
        return -1