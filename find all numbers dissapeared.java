import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;

class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        // Step 1: put all numbers into a HashSet
        HashSet<Integer> set = new HashSet<>();
        for (int n : nums) {
            set.add(n);//set will have time coplexity of one when checking/searching
        }

        // Step 2: check which numbers 1..n are missing
        List<Integer> result = new ArrayList<>();
        for (int i = 1; i <= nums.length; i++) {
            if (!set.contains(i)) {   // like "if i not in nums" in Python
                result.add(i);
            }
        }

        return result;
    }
}
