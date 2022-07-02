class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = 0
        i = 0
        j = 2
        while j <= len(s):
            if i+j <= len(s) and s[i:i+j].count("R") == s[i:i+j].count("L"):
                counter = counter + 1
                i = i+j
                j = 2
                continue
            j = j + 1
        return counter
                