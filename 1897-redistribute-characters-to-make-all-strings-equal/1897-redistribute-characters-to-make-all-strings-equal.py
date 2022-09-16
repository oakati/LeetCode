class Solution(object):
    def makeEqual(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        l_words = len(words)
        m_dict = dict()
        words = "".join(words)
        for ch in words:
            if not m_dict.has_key(ch):
                m_dict[ch] = 1
            else:
                m_dict[ch] = m_dict[ch] + 1
        flag = True
        for a in m_dict.values():
            if a % l_words != 0:
                flag = False
                break
        return flag