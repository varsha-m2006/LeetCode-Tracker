/*PLUS ONE - ARRAYS
PROBLEM 66*/


class Solution {
    public int[] plusOne(int[] digits) {
        int n = digits.length;

        // Start from the end of the array
        for (int i = n - 1; i >= 0; i--) {
            if (digits[i] < 9) {
                // If current digit is less than 9, just add 1 and return
                digits[i]++;
                return digits;
            }
            // If digit is 9, it becomes 0
            digits[i] = 0;
        }

        // If all digits were 9, we need an extra place at the beginning
        int[] result = new int[n + 1];
        result[0] = 1; // 1000... for [9,9,9]
        return result;
    }
}
