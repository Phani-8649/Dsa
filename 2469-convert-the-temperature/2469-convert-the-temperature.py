class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        a=[]
        k=float(celsius)+273.15
        f=float(celsius)*1.80+32.00
        a.append(k)
        a.append(f)
        return a