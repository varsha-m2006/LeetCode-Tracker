/*MINIMUM ADD TO MAKE PARENTHESES VALID - STACKS
PROBLEM 921*/

class Solution {
    public int minAddToMakeValid(String s) {
        Stack<Character> p = new Stack<>();
        int count=0;
        for (char c : s.toCharArray()) {
            //if opening add it in
            if (c == '(' ) {
                p.push(c);
            } 
            else {
                if (p.isEmpty()) count++; 
                else{
                    //top element
                char top = p.pop();
                //if its not equal to opening bracket increment count
                if (c == ')' && top != '(' ) count++;
                }
            }
        }
        //left out elements are added as well
        if(!p.isEmpty()){
            count=count+p.size();
        }

      return count; 
        
    }
}