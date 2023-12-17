class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[]
        b=[]
        c=[]
        for i in nums:
            if(i<0):
                b.append(i)
                # nums.remove(i)
            if(i>0):
                a.append(i)
        for i in range(max(len(a),len(b))):
            if(i<len(a)):
                c.append(a[i])
            if(i<len(b)):
                c.append(b[i])
        return c
