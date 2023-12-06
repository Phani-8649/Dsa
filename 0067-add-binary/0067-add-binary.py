class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        c=int(a,2)+int(b,2)
        c=bin(c)[2:]
        return str(c)