class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        i = 0
        while i < len(word):
            if not word[i].isdigit():
                word = word[:i] + " " + word[i+1:]
            i = i + 1
        return len(set([int(i) for i in word.strip().split()]))