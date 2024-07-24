class Solution(object):
    def sortJumbled(self, mapping, nums):
        """
        :type mapping: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        res=[]
        ans=[]
        for i in nums:
            b=[]
            a=[int(d) for d in str(i)]
            for j in a:
                b.append(mapping[j])
            num=int(''.join(map(str,b)))
            res.append([i,num])
        res.sort(key=lambda x:x[1])
        for i,j in res:
            ans.append(i)
        return ans