class Solution(object):
    def mostFrequent(self, nums, key):
        """
        :type nums: List[int]
        :type key: int
        :rtype: int
        """
        m_dict = dict()
        for i in range(0, len(nums) - 1):
            if nums[i] == key:
                if nums[i+1] in m_dict.keys():
                    m_dict[nums[i+1]] = m_dict[nums[i+1]] + 1
                else:
                    m_dict[nums[i+1]] = 1
        return max(m_dict, key=m_dict.get)