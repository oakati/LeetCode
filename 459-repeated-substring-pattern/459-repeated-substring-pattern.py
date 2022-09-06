class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 1:
            return False
        m_list = [1]
        for i in range(2, len(s)):
            if len(s) % i == 0:
                m_list.append(i)
        print(m_list)
        for i in m_list:
            if s.count(s[:i]) * i == len(s):
                return True
        return False