class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        w_list = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']
        wovels = []
        for i in s:
            if i in w_list:
                wovels.append(i)
        wovels.reverse()
        j = 0
        for i in range(0, len(s)):
            if s[i] in w_list:
                s = s[:i] + wovels[j] + s[i+1:]
                j = j + 1
        return s