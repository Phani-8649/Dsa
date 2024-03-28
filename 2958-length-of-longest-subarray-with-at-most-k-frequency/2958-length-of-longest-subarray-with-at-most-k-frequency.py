class Solution(object):
    def maxSubarrayLength(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        m = {}
        length = 0
        i = 0
        j = 0
        n = len(nums)
        while j < n:
            m[nums[j]] = m.get(nums[j], 0) + 1
            while m[nums[j]] > k:
                m[nums[i]] -= 1
                i += 1
            length = max(length, j - i + 1)
            j += 1
        return length