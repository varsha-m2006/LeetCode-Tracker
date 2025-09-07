/*TIME NEEDED TO BUY TICKETS - QUEUE
PROBLEM 2073*/

class Solution {
    public int timeRequiredToBuy(int[] tickets, int k) {
        int n=tickets.length;
        Queue <Integer> index= new LinkedList<>();
        int count=0;
        //adding all into queue
        for(int i=0;i<n;i++){
            index.add(i);
        }
        //to make it cyclic 
        while(!index.isEmpty()){
            //peak element
            int person=index.poll();
            //subtracting tickets and adding time seconds
            tickets[person]--;
            count++;
            
            //push it back in queue if tickets still left
            if(tickets[person]!=0){
                index.add(person);
            }
            //if tickets of k position is done return total time
            if(tickets[k]==0 && k==person){
                return count;
            }
        }
        return count;
        
    }
}