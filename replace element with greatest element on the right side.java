/*REPLACE ELEMENTS WITH GREATEST ELEMENT ON RIGHT SIDE - ARRAYS
PROBLEM 1299*/

class Solution {
    public int[] replaceElements(int[] arr) {
        //iterating through array
        for(int i=0;i<arr.length;i++){
            //initializing as 0
            int max=0;
            //indication of whether its found or not
            int c=1;
            //finding largest element after current
            for(int j=i+1;j<arr.length;j++){
                //found
                if(arr[j]>max){
                    max=arr[j];
                    c=0;
                }
            }
            //not found
            if(c==1){
                arr[i]=-1;
            }
            //found
            else{
                arr[i]=max;
            }


        }
        //returninh modified array
        return arr;
        
    }
}