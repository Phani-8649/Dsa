class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l=0
        r=1
        mp=0
        while(r<len(prices)):
            if(prices[l]<prices[r]):
                p=prices[r]-prices[l]
                mp=max(mp,p)
            else:
                l=r
            r=r+1
        return mp