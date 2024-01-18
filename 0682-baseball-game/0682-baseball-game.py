class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        a = []  # Initialize an empty list to represent the stack
        
        for i in operations:
            if i == "C":
                if a:
                    a.pop()
            elif i == "D":
                a.append(2 * int(a[-1]))
            elif i == "+":
                a.append(int(a[-1]) + int(a[-2]))
            else:
                a.append(int(i))
        
        return sum(a)
