class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s.split(" ")
        for i in range(0,len(s)):
            s[i] = s[i][-1] + s[i][:len(s[i])-1]
        s.sort();
        for i in range(0,len(s)):
            s[i] = s[i][1:]
        return " ".join(s)
