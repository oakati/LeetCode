class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        m_arr = []
        val = nums[0]
        m_arr.append(val % 5 == 0)
        for i in range(1,len(nums)):
            val = val*2+nums[i]
            m_arr.append(val % 5 == 0)
        return m_arr