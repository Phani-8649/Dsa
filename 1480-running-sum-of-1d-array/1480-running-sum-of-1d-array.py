class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[]
        s=0
        for i in nums:
            s=s+i
            l.append(s)
        del nums[:]
        for i in l:
            nums.append(i)
        return nums