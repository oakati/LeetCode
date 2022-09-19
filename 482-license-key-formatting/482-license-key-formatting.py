import math
class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = "".join(s.split("-"))
        res = math.floor(len(s) / k)
        rem = len(s) % k
                
        start = 0
        end = rem
        s_final = s[start:end].upper()

        start = start + rem
        end = end + k
        while end <= len(s):
            if s_final != "":
                s_final = s_final + "-"
            for j in range(start, end):
                temp = s[j]
                if temp.islower():
                    temp = temp.upper()
                s_final = s_final + temp
            start = start + k
            end = end + k
        return s_final