class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums,i=set(nums),1
        while i<=2147483647:
            if i not in nums:   return i
            i+=1