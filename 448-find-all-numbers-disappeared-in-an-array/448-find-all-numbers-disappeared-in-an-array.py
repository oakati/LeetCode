class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        myarray = list(range(1,len(nums)+1))
        return set(myarray)-set(nums)