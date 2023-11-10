class Solution(object):
    def findMiddleIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ts=sum(nums)
        ls=0
        for i in range(len(nums)):
            ts=ts-nums[i]
            if(ls==ts):
                return i
            ls=ls+nums[i]
        return -1
        