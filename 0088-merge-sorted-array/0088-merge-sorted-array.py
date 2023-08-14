class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        l=[]
        for i in range(0,m):
            l.append(nums1[i])
        for j in range(0,n):
            l.append(nums2[j])
        del nums1[:]
        for i in l:
            nums1.append(i)
        nums1.sort()
        