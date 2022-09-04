class Solution(object):

    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def non_decreasing(L):
            return all(x<=y for x, y in zip(L, L[1:]))
        m_list = []
        for j in range(2,len(nums)+1):
            for i in itertools.combinations(nums,j):
                m_list += [i]
        return [list(i) for i in set(m_list) if non_decreasing(list(i)) == True]