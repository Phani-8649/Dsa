class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        c=0
        s="abcdefghijklmnopqrstuvwxyz"
        for i in s:
            if(i in sentence):
                c+=1
        if(c==len(s)):
            return True
        return False
