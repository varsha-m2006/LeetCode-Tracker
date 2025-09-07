/*MAX CONSECUTIVE ONES III - ARRAYS AND SLIDING POINT
PROBLEM 1004*/

class Solution {
    public int longestOnes(int[] nums, int k) {
        int left = 0;
        int zeroCount = 0;
        int maxLen = 0;
        
        for (int right = 0; right < nums.length; right++) {
            if (nums[right] == 0) {
                zeroCount++;
            }
            
            // Shrink window if zeros > 1
            while (zeroCount > k) {
                if (nums[left] == 0) {
                    zeroCount--;
                }
                left++;
            }
            
            // Update max length
            if (maxLen<right-left+1){
            	
            	maxLen=right-left+1;
            	
            }
            	
            }
        
        
        return maxLen;
    }
}