class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=[]
        b=[]
        for i in range(len(nums)):
            if(nums[i]%2==0):
                b.append(nums[i])
        if not b:
            return -1
        b=sorted(b)
        c=Counter(b)
        for i in b:
            if(c[i]==max(c.values())):
                return i
