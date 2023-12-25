class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(2>n):
            greater=2
        else:
            greater=n
        while(True):
            if(greater %2 ==0 and (greater%n==0)):
                lcm=greater
                break
            greater+=1
        return lcm