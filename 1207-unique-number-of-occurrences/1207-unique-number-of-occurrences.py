class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        m_dict = dict()
        
        for i in arr:
            if not m_dict.has_key(i):
                m_dict[i] = 1
            else:
                m_dict[i] = m_dict[i] + 1
        
        return len(m_dict.values()) == len(set(m_dict.values()))