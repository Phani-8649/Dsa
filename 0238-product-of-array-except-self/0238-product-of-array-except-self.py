class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[1]*(len(nums))
        pre=1
        for i in range(len(nums)):
            a[i]=pre
            pre=pre*nums[i]
        post=1
        for j in range(len(nums)-1,-1,-1):
            a[j]=a[j]*post
            post=post*nums[j]
        return a