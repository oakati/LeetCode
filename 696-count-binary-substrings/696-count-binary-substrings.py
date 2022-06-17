from itertools import groupby
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = [len(''.join(g).encode("utf-8")) for _, g in groupby(s)]
        counter = 0
        for i in range(0,len(a)-1):
            counter = counter + min(a[i],a[i+1])
        return counter