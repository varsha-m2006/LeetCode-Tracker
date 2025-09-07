/*REMOVE ELEMENT - ARRAYS
PROBLEM 27*/

class Solution {
    public int removeElement(int[] nums, int val) {
        
        
        //the pointer to recognize target values
        int i=0;
        //number of non-target values
        int c=0;
        //to iterate accross the array
        for (int j=0;j<nums.length;j++){
            //if we are at target value and next element is non target value you swap and increment i pointer
            if (nums[j]!=val){
                if(nums[i]==val){
                    
                    int temp=nums[j];
                    nums[j]=nums[i];
                    nums[i]=temp;
                    i++;
                    
            }
            //incrementation of i pointer
            if(nums[i]!=val){
                i++;
            }
            
            }
        
        }
        //number of non target values
        for(int j=0;j<nums.length;j++){
            if(nums[j]!=val){
                c++;
            }
        }

        return c;
    }
}