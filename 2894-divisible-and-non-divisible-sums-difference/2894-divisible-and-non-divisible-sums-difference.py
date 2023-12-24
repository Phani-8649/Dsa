class Solution(object):
    def differenceOfSums(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        a=[]
        b=[]
        c=[]
        for i in range(1,n+1):
            a.append(i)
        for i in a:
            if(i%m==0):
                b.append(i)
            else:
                c.append(i)
        return (sum(c)-sum(b))