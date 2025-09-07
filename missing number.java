/*MISSING NUMBER - ARRAYS
PROBLEM 268*/

class Solution {
    public int missingNumber(int[] nums) {
        int sum=0;
        //finding the actual sum
        for(int i=0;i<nums.length;i++){
            sum=sum+nums[i];
        }
        int n=nums.length;
        //subtracting it from the expected sum which is sum of first n natural numbers
        return ((n*(n+1))/2)-sum;
        
    }
}