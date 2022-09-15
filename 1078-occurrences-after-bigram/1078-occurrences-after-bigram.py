class Solution(object):
    def findOcurrences(self, text, first, second):
        """
        :type text: str
        :type first: str
        :type second: str
        :rtype: List[str]
        """
        m_arr = []
        s_text = text.split(" ")
        for i in range(0,len(s_text)-2):
            if s_text[i] == first and s_text[i+1] == second:
                m_arr.append(s_text[i+2])
        return m_arr
        