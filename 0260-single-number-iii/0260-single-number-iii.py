class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = {}
    
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        

        res = [num for num in count if count[num] == 1]
        
        return res