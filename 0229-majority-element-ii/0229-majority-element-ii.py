class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[]
        n=list(set(nums))
        for i in n:
            if(nums.count(i)>(len(nums)//3)):
                a.append(i)
        return a