class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        j=0
        a=[]
        for i in range(1,len(nums)):
            if(nums[j]==nums[i]):
                nums[j]=nums[j]*2
                nums[i]=0
            j+=1
        for i in nums:
            if(i!=0):
                a.append(i)
        n=len(nums)-len(a)
        res=a+[0]*n
        return res