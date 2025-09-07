/*DOTA2 SENATE - QUEUE
PROBLEM 649*/

class Solution {
    public String predictPartyVictory(String senate) {
        //storing both parties
        Queue <Integer> radiant = new LinkedList<>();
        Queue <Integer> dire = new LinkedList<>();
        //updating arrays
         for (int i = 0; i < senate.length(); i++) {
            if (senate.charAt(i) == 'R') radiant.add(i);
            else dire.add(i);
        }

        //iterating
        while(!radiant.isEmpty() && !dire.isEmpty()){
            int indexR=radiant.poll();
            int indexD=dire.poll();
            //checking which index is greater
            if(indexR>indexD){
                dire.add(indexD+senate.length());
            }
            else{
                radiant.add(indexR+senate.length());
            }
        }
        //whichever is not empty is the winner
        return radiant.isEmpty() ? "Dire" : "Radiant";
    }
}