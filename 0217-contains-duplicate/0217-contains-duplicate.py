class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l=set(nums)
        l1=list(l)
        if(len(nums)!=len(l1)):
            return True
        else:
            return False