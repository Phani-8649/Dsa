class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n<=0):
            return False
        a=(log(n,3))
        print(a)
        print(int(a))
        if(3**(round(a))==n):
            return True