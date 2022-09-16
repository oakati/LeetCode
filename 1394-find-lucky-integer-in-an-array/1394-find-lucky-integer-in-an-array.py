class Solution(object):
    def findLucky(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr = sorted(arr)
        for i in range(len(arr)-1,-1,-1):
            if arr.count(arr[i]) == arr[i]:
                return arr[i]
        return -1