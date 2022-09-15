class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """
        counter = 0
        for pattern in patterns:
            if pattern in word:
                counter = counter + 1
        return counter