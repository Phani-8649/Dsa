class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        c=0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(abs(nums[i]-nums[j])==k):
                    print(nums[i],nums[j])
                    c+=1
        return c