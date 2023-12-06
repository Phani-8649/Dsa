class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = n / 7
        b = n % 7
        ans = ((float(a) / 2) * (2 * (28) + (a - 1) * 7)) + ((float(b) / 2) * (2 * (a + 1) + (b - 1)))
        return int(ans)
