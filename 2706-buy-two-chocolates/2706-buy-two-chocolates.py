class Solution(object):
    def buyChoco(self, prices, money):
        """
        :type prices: List[int]
        :type money: int
        :rtype: int
        """
        prices=sorted(prices)
        print(prices)
        return money-sum(prices[:2]) if (money-sum(prices[:2]))>=0 else money