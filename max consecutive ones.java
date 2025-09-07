/*MAX CONSECUTIVE ONES - ARRAYS
PROBLEM 485*/

class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        
        //initializing max=0
        int max=0;
        //iterating through array
        for(int i =0;i<nums.length;i++){
            //initializing counter as 0
            int c=0;
            //till 0 is encountered counter is incremented
            while (nums[i]!=0){

                c++;
                //maximum value updated
                if (max<c){
                    max=c;
                }
                //to avoid out of bound error
                if (i<nums.length-1){
                    i++;
                }
                else{
                    break;
                }
            }
        }
        //returning output
        return max;
        
    }
}