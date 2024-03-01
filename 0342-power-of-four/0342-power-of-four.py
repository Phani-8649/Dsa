class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n<=0):
            return False
        a=int(log(n,4))
        print(a)
        if(4**a==n):
            return True