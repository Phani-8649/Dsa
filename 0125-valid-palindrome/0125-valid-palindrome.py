class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=''.join(i for i in s if i.isalnum())
        s=s.lower()
        ss=''.join(reversed(s))
        if(s==ss):
            return True
        else:
            return False