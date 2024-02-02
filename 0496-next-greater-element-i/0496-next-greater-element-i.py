# class Solution(object):
#     def nextGreaterElement(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: List[int]
#         """
#         res=[]
#         for i in nums1:
#             n=nums2.index(i)
#             # print(n)
#             if(n+1==len(nums2)):
#                 res.append(-1)
#             elif(nums2[n]<nums2[n+1]):
#                 res.append(nums2[n+1])
#             else:
#                 res.append(-1)
#         return res
class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for i in nums1:
            n = nums2.index(i)
            found = False
            
            for j in range(n + 1, len(nums2)):
                if nums2[j] > i:
                    res.append(nums2[j])
                    found = True
                    break
            
            if not found:
                res.append(-1)
                
        return res
