class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = list(s.encode("utf-8"))
        record = 0
        for i in range(0,len(a)):
            for j in range(i+record,len(a)+1):
                if len(set(a[i:j])) < len(a[i:j]):
                    break
                    
                if len(set(a[i:j])) == len(a[i:j]):
                    record = max(record,len(a[i:j]))
        return record