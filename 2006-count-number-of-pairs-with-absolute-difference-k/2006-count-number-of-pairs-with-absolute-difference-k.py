class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sum([max(list(i)) - min(list(i)) == k for i in itertools.combinations(nums,2)])