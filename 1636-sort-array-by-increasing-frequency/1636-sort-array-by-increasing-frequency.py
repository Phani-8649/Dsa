class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        a=[]
        for i in list(set(nums)):
            a.append([i,nums.count(i)])
        a.sort(key=lambda x: (x[1], -x[0]))
        for i,j in a:
            res.extend([i]*j)
        return res