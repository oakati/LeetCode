class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        lim = min(len(str1), len(str2))
        for i in range(lim, 0, -1):
            if (str1[:i] == str2[:i]) and (str1.count(str1[:i])*i == len(str1)) and (str2.count(str2[:i])*i == len(str2)):
                return str1[:i]
        return ""
