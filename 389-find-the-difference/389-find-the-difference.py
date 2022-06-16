class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    t = t[:j] + t[j+1:]
                    break
        return t
       