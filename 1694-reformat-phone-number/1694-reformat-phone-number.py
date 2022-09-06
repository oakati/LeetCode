class Solution(object):
    def reformatNumber(self, number):
        """
        :type number: str
        :rtype: str
        """
        number = number.replace(" ","-").split("-")
        number = "".join(number)
        i = 0
        m_number = ""
        while i < len(number):
            if i == len(number) - 4:
                m_number = m_number + "-" + number[i:i+2] + "-" + number[i+2:i+4]
                break
            elif i == len(number) - 3 or i == len(number) - 2:
                m_number = m_number + "-" + number[i:i+(len(number)-i)]
                break
            m_number = m_number + "-" + number[i:i+3]
            i = i + 3
        return m_number[1:]