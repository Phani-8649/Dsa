class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        c1=0
        c2=0
        mp=len(s)//2
        s1=s[:mp]
        s2=s[mp:]
        vowels="aeiouAEIOU"
        for i in s1:
            if(i in vowels):
                c1+=1
        for i in s2:
            if(i in vowels):
                c2+=1
        return c1==c2
        