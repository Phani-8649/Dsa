# class Solution:
#     def numSubarrayProductLessThanK(self, nums, k):
#         ans = 0
#         for i in range(len(nums)):
#             t = 1
#             for j in range(i, len(nums)):
#                 t *= nums[j]
#                 if t < k:
#                     ans += 1
#                 else:
#                     break
#         return ans

class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1:
            return 0
        
        ans = 0
        left = 0
        product = 1
        
        for right in range(len(nums)):
            product *= nums[right]
            
            while product >= k:
                product /= nums[left]
                left += 1
            
            ans += right - left + 1
        
        return ans