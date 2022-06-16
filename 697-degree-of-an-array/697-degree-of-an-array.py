class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = len(nums)
        out = []
        d={}
        for i in nums:
            if i not in d:
                d[i] = nums.count(i)
        max_freq = max(d.values())
        for i in d.keys():
            if d[i] != max_freq:
                d.pop(i,None)
        for j in d.keys():
            out = []
            for i in range(len(nums)):
                if nums[i] == j:
                    out.append(i)
            result = min(result,max(out)-min(out)+1)
        return result
        
            
