class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        ans = 0
        n = len(nums)
        for i in range(n):
            if nums[i] + diff in nums and nums[i] + 2 * diff in nums:
                ans += 1
        
        return ans