class Solution(object):
    def winningPlayerCount(self, n, pick):
        """
        :type n: int
        :type pick: List[List[int]]
        :rtype: int
        """
        d={}
        res=[]
        pc=0
        for p, c in pick:
            if p not in d:
                d[p] = {}
            if c not in d[p]:
                d[p][c] = 0
            d[p][c] += 1
        for i in range(n):
            if any(count > i for count in d.get(i, {}).values()):
                pc += 1
        return pc