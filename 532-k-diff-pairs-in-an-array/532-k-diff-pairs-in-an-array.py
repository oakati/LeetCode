from scipy.special import comb
class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        uniquenums = list(set(nums))
        count = 0
        if k == 0:
            for i in uniquenums:
                if nums.count(i) > 1:
                    count += 1
            return int(count)
        for i in range(len(uniquenums)):
            if uniquenums[i]+k in uniquenums and k != 0:
                count += 1
        return count
                
            