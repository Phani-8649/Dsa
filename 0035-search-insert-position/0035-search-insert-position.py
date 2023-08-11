class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if(target in nums):
                if(nums[i]==target):
                    return i
            elif(target>nums[len(nums)-1]):
                return len(nums)
            else:
                if(nums[i]>target):
                    return i
        return 0