class Solution(object):
    def countVowelSubstrings(self, word):
        """
        :type word: str
        :rtype: int
        """
        counter = 0
        m_list = ['a', 'e', 'i', 'o', 'u']
        for i in range(0,len(word)):
            for j in range(i + 1, len(word)+1):
                flag = False
                for k in m_list:
                    if k not in word[i:j]:
                        flag = True
                        break
                for k in word[i:j]:
                    if k not in m_list:
                        flag = True
                        break                
                if flag == False:
                    counter = counter + 1
        return counter