/*IMPLEMENT QUEUE USING STACKS - STACKS AND QUEUES
PROBLEM 232(JAVA)*/

class MyQueue {
    //we have two stacks one stack for the elements and one helper
    private Stack<Integer> first;
    private Stack<Integer> second;

    public MyQueue() {

        //constructor
        first=new Stack<>();
        second = new Stack<>();
       
    }

    
    
    public void push(int x) {
        //pusihing is same for queues and stacks
        first.push(x);
        
    }
    
    public int pop() {
        //push all the elements in first stack into the other reversing the order
        while(!first.isEmpty()){
            second.push(first.pop());
        }
        //popping out top element
        int removed= second.pop();
        //the push all back in
        while(!second.isEmpty()){
            first.push(second.pop());
        }

        return removed;
        
    }
    
    public int peek() {
        //similarly for peek its just hear we dont pop
        while(!first.isEmpty()){
            second.push(first.pop());
        }

        int removed= second.peek();

        while(!second.isEmpty()){
            first.push(second.pop());
        }

        return removed;
    }
    
    public boolean empty() {
        //in built function 
        return first.isEmpty();
        
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */