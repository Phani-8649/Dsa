class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_current=max_result=nums[0]
        for i in nums[1:]:
            max_current=max(i,max_current+i)
            max_result=max(max_current,max_result)
        return max_result
