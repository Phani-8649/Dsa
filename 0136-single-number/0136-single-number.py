class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=[]
        for i in range(0,len(nums)):
            if((nums.count(nums[i]))>1):
                l.append(nums[i])
        for i in nums:
            if(i not in l):
                return (i)