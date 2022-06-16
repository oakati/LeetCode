class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mysums = 0
        count = 0
        d = {0:1}
        for i in range(len(nums)):
            mysums += nums[i]
            
            if mysums-k in d:
                count += d[mysums-k]
            if mysums not in d:
                d[mysums] = 1
            elif mysums in d:
                d[mysums] +=1
        return count
                    