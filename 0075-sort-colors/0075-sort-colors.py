class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if(nums[i]>nums[j]):
                    t=nums[i]
                    nums[i]=nums[j]
                    nums[j]=t
        return nums