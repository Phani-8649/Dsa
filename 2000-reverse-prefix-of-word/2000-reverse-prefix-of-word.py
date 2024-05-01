class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        res=""
        k=0
        for i in word:
            if(i==ch):
                k=word.index(i)
        for i in word[k::-1]:
            res+=i
        for j in word[k+1:]:
            res+=j
        return res
        