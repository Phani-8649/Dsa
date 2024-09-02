class Solution(object):
    def chalkReplacer(self, chalk, k):
        """
        :type chalk: List[int]
        :type k: int
        :rtype: int
        """
        k=k%sum(chalk)
        n=len(chalk)
        i=0
        while True:
            k-=chalk[i]
            if(k<0):
                return i
            i=(i+1)%n