class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        counter = 0
        for word in words:
            for length in range(1,len(word)+1):
                if word[length-1] != word[length-1]:
                    break
                elif pref == word[:length]:
                    counter = counter + 1
        return counter