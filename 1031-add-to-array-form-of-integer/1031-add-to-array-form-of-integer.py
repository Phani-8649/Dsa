class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        a=[]
        n=0
        for i in num:
            n=n*10+i
        ans=n+k
        while ans>0:
            h=ans%10
            a.append(h)
            ans=ans//10
        return reversed(a)