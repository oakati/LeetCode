class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        counter = 0
        s_num = str(num)
        for i in range(0,len(s_num)-k+1):
            if (int(s_num[i:i+k]) == 0):
                continue
            if(num % int(s_num[i:i+k])== 0):
                counter = counter + 1
        return counter
        