class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=list(set(nums))
        for i in n:
            if((nums.count(i)>len(nums)//2)):
                return i