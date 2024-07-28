class Solution(object):
    def canAliceWin(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s1=0
        s2=0
        for i in range(len(nums)):
            if(len(str(nums[i]))==1):
                s1+=nums[i]
            elif(len(str(nums[i]))==2):
                s2+=nums[i]
        return not s1==s2