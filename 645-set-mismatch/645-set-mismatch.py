from statistics import mode
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        m = mode(nums)
        diff = sum(nums) - (len(nums)*(len(nums)+1)/2)
        return [m, int(m - diff)]