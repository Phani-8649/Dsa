class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s=0
        l=[]
        l1=[]
        for i in range(0,len(digits)):
            s=s+(digits[i]*pow(10,len(digits)-i-1))
        s=s+1
        while(s>0):
            r= s % 10
            l.append(r)
            s=s/10
        l.reverse()
        return l
        
        