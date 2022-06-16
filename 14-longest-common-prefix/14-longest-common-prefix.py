class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        record = 0
        for i in strs:
            if len(i)>record:
                record = len(i)
        prefix = 0
        for i in range(1,record+1):
            flag = True
            for j in strs:
                if strs[0][:i]!=j[:i]:
                    flag=False
                    break
            if flag == True:
                prefix = i
        if len(strs) == 1:
            return strs[0]
        elif prefix == 0:
            return ""
        else:
            print(prefix)
            return strs[0][:prefix]
                