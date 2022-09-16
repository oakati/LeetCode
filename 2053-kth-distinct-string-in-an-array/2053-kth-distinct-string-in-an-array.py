class Solution(object):
    def kthDistinct(self, arr, k):
        """
        :type arr: List[str]
        :type k: int
        :rtype: str
        """
        counter = 0
        for i in arr:
            if arr.count(i) == 1:
                counter = counter + 1
                if counter == k:
                    return i
        return ""
        