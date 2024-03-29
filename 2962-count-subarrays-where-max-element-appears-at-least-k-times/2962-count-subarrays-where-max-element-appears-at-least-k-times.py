class Solution(object):
    def countSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        c=0
        m=max(nums)
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i:j+1].count(m)>=k):
                    c+=1
        return c