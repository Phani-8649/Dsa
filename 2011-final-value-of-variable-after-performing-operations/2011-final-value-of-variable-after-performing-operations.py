class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        c=0
        for i in operations:
            if(i[0]=="+" or i[-1]=="+"):
                c+=1
            else:c-=1
        return c
        