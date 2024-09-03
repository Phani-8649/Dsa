class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        a=[]
        r=""
        alphabet="abcdefghijklmnopqrstuvwxyz"
        for i in s:
            r=r+str(alphabet.index(i)+1)
        for i in range(k):
            o=sum(int(digits) for digits in r)
            r=str(o)
        return o