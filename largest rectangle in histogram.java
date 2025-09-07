/*LARGEST RECTANGLE IN HISTOGRAM - STACKS
PROBLEM 84*/

class Solution {
    public int largestRectangleArea(int[] heights) {
        //having a monotonic stack
        Stack<Integer> index = new Stack<>();
        //initializing as 0
        int max = 0;
        //iterating through heights
        for (int i = 0; i < heights.length; i++) {
            //if your encountering incoming element as lesser than peek
            while (!index.isEmpty() && heights[index.peek()] > heights[i]) {
                //pop it out
                int element = index.pop();
                //next smaller element
                int nse = i;
                //previous smaller element
                int pse;
                //if empty initialized to -1
                if (index.isEmpty()) {
                    pse = -1;
                } 
                //peek index
                else {
                    pse = index.peek();
                }
                //area calculated
                max = Math.max(heights[element] * (nse - pse - 1), max);
            }
            //pushing in index
            index.push(i); 
        }

        // cleanup pass
        while (!index.isEmpty()) {
            int element = index.pop();
            int nse = heights.length;
            int pse;
            if (index.isEmpty()) {
                pse = -1;
            } else {
                pse = index.peek();
            }
            max = Math.max(heights[element] * (nse - pse - 1), max);
        }

        return max;
    }
}
