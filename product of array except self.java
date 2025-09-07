/*PRODUCT OF ARRAY EXCEPT SELF - ARRAYS
PROBLEM 238*/

class Solution {
    public int[] productExceptSelf(int[] nums) {
        //result
        int [] o=new int[nums.length];
        //length
        int n = nums.length;

        //initializing as 1
        o[0]=1;
        //prefix product
        for(int i=1;i<n;i++){
            o[i]=o[i-1]*nums[i-1];
        }
        //suffix product
        int suffix=1;
        for(int i=n-1;i>=0;i--){
            o[i]*=suffix;
            suffix*=nums[i];
        }
        //returning output
        return o;
        
    }
}