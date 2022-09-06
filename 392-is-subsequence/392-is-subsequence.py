class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        while i < len(s):
            if i < len(t) and s[i] != t[i]:
                t = t[:i] + t[i+1:]
                continue
            else:
                i = i + 1
        return s in t
