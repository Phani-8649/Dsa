class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l=[]
        l1=[]
        l2=[]
        for i in nums:
            l.append(i)
        for i in l:
            if(i==0):
                l1.append(i)
            else:
                l2.append(i)
        del nums[:]
        for i in l2:
            nums.append(i)
        for i in l1:
            nums.append(i)