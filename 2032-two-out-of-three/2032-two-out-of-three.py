class Solution(object):
    def twoOutOfThree(self, nums1, nums2, nums3):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type nums3: List[int]
        :rtype: List[int]
        """
        m_arr = []
        for i in nums1:
            if i in nums2 or i in nums3:
                m_arr.append(i)
        for i in nums2:
            if i in nums1 or i in nums3:
                m_arr.append(i)
        return set(m_arr)