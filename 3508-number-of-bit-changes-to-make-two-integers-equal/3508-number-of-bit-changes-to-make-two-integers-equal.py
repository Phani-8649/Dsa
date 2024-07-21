class Solution(object):
    def minChanges(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        res=0
        if n<k:
            return -1
        elif n&k!=k:
            return -1
        else:
            res=bin(n).count("1")-bin(k).count("1")
        return res