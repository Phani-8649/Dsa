class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if(num==1):return True
        l,r=1,num//2
        while(l<=r):
            mid=l+(r-l)//2
            square=mid*mid
            if(square==num):
                return True
            elif(square<num):
                l=mid+1
            elif(square>num):
                r=mid-1
        return False