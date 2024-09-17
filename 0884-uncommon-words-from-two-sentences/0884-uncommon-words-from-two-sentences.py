class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        res=[]
        one=s1.split()
        two=s2.split()
        for i in one:
            if(i not in two and one.count(i)==1):
                res.append(i)
        for i in two:
            if(i not in one and two.count(i)==1):
                res.append(i)
        return set(list(res))