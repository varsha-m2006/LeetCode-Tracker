/*DUPLICATE ZEROS - ARRAYS
PROBLEM 1089*/

class Solution {
    public void duplicateZeros(int[] arr) {
        int in=1;
        for(int i=0;i<arr.length;i=i+in){
            //if zero is found
            if (arr[i]==0){
                //right shift
                for(int j=arr.length-1;j>i+1;j--){
                    arr[j]=arr[j-1];
                }
                //putting zero in left out space
                if(i!=arr.length-1){
                    arr[i+1]=0;
                    //to avoid other elements as intializied to 0
                    in=2;
                }
            }
            else{
                in=1;
            }
        }
        
    }
}