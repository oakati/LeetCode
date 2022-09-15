class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res = "".join([str(ord(i)-96) for i in s])
        i = 0
        while i < k:
            val = 0
            for j in res:
                val = val + int(j)
            res = str(val)
            i = i + 1
        return val