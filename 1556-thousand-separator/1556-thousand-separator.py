class Solution(object):
    def thousandSeparator(self, n):
        """
        :type n: int
        :rtype: str
        """
        n = str(n)[::-1]
        m_str = ""
        for i in range(0,len(n)):
            m_str = n[i] + m_str
            if i % 3 == 2 and i != len(n) - 1:
                m_str = "." + m_str
        return m_str
