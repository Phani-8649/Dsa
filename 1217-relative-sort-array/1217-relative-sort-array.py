class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        res=[]
        for i in arr2:
            res.extend([i]*arr1.count(i))
        arr1.sort()
        for i in arr1:
            if(i not in res):
                res.extend([i]*arr1.count(i))
        return res