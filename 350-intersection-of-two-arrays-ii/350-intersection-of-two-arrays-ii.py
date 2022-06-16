class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        out = []
        
        for i in nums1:
            if i in nums2 and i not in out:
                for j in range(min(nums1.count(i),nums2.count(i))):
                    out.append(i)        
        return out