class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=[]
        num=list(set(nums))
        for i in num:
            res.append(nums.count(i))
        a=max(res)
        b=res.count(a)
        return a*b