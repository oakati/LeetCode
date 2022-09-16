class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr = sorted(arr)
        print arr
        diff = arr[1] - arr[0]
        for i in range(1,len(arr)-1):
            if diff != arr[i+1]-arr[i]:
                return False
        return True