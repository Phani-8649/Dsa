class Solution {
    public int[] twoSum(int[] nums, int target) {
        int i,j;
        int n=nums.length;
        int[] sumArray= new int[2];
        for(i=0;i<n;i++)
        {
            for(j=i+1;j<n;j++)
            {
                if(nums[i]+nums[j]==target)
                {
                    sumArray[0]=i;
                    sumArray[1]=j;
                }
            }
        }
        return sumArray;
    }
}