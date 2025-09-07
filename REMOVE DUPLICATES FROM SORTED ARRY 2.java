/*REMOVE DUPLICATES FROM SORTED ARRAY II - ARRAYS
PROBLEM 80*/

class Solution {
    public int removeDuplicates(int[] nums) {
        int n = nums.length;
        if (n <= 2) return n; // Already fine if <= 2

        int i = 2; // i = index where we write next valid element

        for (int j = 2; j < n; j++) {
            // compare current with element 2 places behind
            if (nums[j] != nums[i - 2]) {
                nums[i] = nums[j];
                i++;
            }
        }
        return i; // new length
    }
}
