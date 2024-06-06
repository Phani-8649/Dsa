class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res=[]
        d1={chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
        for i in words[0]:
            for j in i:
                d1[j]+=1
        for i in words[1:]:
            d2={chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
            for j in i:
                d2[j]+=1
            for j in d1:
                d1[j]=min(d1[j],d2[j])
        for i in d1:
            if(d1[i]>0):
                res.extend(i*d1[i])
                # extend adds element in each iteration
                # append adds element at the end
        return res