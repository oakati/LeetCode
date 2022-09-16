class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m_dict = dict()
        
        for num in nums:
            if not m_dict.has_key(num):
                m_dict[num] = 0
            else:
                return num