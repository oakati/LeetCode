class Solution(object):
    def isPrefixString(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        for i in range(1,len(words)+1):
            if s == "".join(words[:i]):
                return True
        return False