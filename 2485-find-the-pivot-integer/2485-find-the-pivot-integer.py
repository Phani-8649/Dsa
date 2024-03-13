class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        res=[]
        j=0
        for i in range(1,n+1):
            res.append(i)
        while(j<n):
            if(sum(res[:j+1])==sum(res[j:])):
                return j+1
            j+=1
        return -1