class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        m=1
        a=[int(i) for i in str(n)]
        for i in a:
            m=m*i
        s=sum(a)
        return (m-s)
        