class Solution(object):
    def sumBase(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        res=""
        ans=0
        while n>0:
            r=n%k
            res=str(r)+res
            n=n//k
        for i in res:
            ans=int(i)+ans
        return ans