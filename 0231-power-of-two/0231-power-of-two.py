class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n<=0):
            return False
        a=int(log(n,2))
        print(a)
        if(2**a==n):
            return True