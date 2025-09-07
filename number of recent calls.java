/*NUMBER OF RECENT CALLS - QUEUE
PROBLEM 933*/

class RecentCounter {
    //initializing queue
    Queue<Integer> counter;

    public RecentCounter() {
        counter = new LinkedList<>();
    }
    
    public int ping(int t) {
        //pushing in
        counter.add(t);
        //if not range popped out
        while (!counter.isEmpty() && counter.peek() < t - 3000) {
            counter.poll();
        }
        //the counter returned
        return counter.size();
    }
}
 