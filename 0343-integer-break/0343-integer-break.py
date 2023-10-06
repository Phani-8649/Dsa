class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n<=3):
            return n-1
        qu,rem=divmod(n,3)
        if(rem==0):
            return 3**qu
        elif(rem==1):
            return (3**(qu-1))*4
        else:
            return (3**qu)*2
