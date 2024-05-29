class Solution(object):
    def numSteps(self, s):
        """
        :type s: str
        :rtype: int
        """
        c=0
        num=int(s,2)
        while(num>1):
            if(num%2!=0):
                num=num+1
                c+=1
            elif(num%2==0):
                num=num/2
                c+=1
        return c