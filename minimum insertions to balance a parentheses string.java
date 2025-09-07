/*MINIMUM INSERTIONS TO BALANCE A PARENTHESES STRING
PROBLEM 1541*/

class Solution {
    public int minInsertions(String s) {
        int res = 0;   // insertions
        int need = 0;  // number of ')' we still need

        for (char c : s.toCharArray()) {
            if (c == '(') {
                need += 2; // '(' needs 2 ')'

                // if need is odd, we must insert one ')'
                if (need % 2 == 1) {
                    res++;
                    need--; 
                }
            } else { // c == ')'
                need--; 

                if (need < 0) {
                    // too many ')', insert '('
                    res++;
                    need = 1; // now this ')' is half-satisfied
                }
            }
        }

        return res + need; // add any remaining ')'
    }
}
