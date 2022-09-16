class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        m_pocket = dict()
        m_pocket["5"] = 0
        m_pocket["10"] = 0
        m_pocket["20"] = 0

        for bill in bills:
            if bill == 5:
                m_pocket["5"] = m_pocket["5"] + 1
            elif bill == 10:
                m_pocket["10"] = m_pocket["10"] + 1
                if m_pocket["5"] != 0:
                    m_pocket["5"] = m_pocket["5"] - 1
                else:
                    return False
            elif bill == 20:
                m_pocket["20"] = m_pocket["20"] + 1
                if m_pocket["10"] != 0 and m_pocket["5"] != 0:
                    m_pocket["5"] = m_pocket["5"] - 1
                    m_pocket["10"] = m_pocket["10"] - 1
                elif m_pocket["5"] >= 3:
                    m_pocket["5"] = m_pocket["5"] - 3
                else:
                    return False
        return True
