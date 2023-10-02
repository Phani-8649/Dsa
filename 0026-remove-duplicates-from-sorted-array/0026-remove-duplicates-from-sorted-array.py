class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=list(set(nums))
        del nums[:]
        nums.extend(res)
        nums.sort()
        return len(nums)