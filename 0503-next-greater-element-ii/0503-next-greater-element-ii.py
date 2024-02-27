class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Concatenate nums with itself to make it circular
        nums *= 2
        n = len(nums)
        
        s = []
        ans = [-1] * (n // 2)  # Initialize ans with -1 for each element
        
        # Traverse the circular list in reverse order
        for i in range(n - 1, -1, -1):
            # While stack is not empty and the current element is greater than the top element of the stack
            while s and s[-1] <= nums[i]:
                s.pop()
            # If stack is empty, there's no greater element to the right
            if not s:
                # For circular list, the index in the original list is (i % (n // 2))
                ans[i % (n // 2)] = -1
            else:
                # For circular list, the index in the original list is (i % (n // 2))
                ans[i % (n // 2)] = s[-1]
            s.append(nums[i])  # Push current element onto the stack
        
        return ans
