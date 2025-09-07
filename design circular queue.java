/*DESIGN CIRCULAR QUEUE - QUEUE
PROBLEM 622*/

class MyCircularQueue {
    private int[] data;
    private int front;
    private int rear;
    private int count;
    private int size;

    public MyCircularQueue(int k) {
        data = new int[k];
        size = k;
        front = 0;
        rear = -1; // rear starts before the first index
        count = 0;
    }
    
    public boolean enQueue(int value) {
        if (isFull()) return false;
        rear = (rear + 1) % size;
        data[rear] = value;
        count++;
        return true;
    }
    
    public boolean deQueue() {
        if (isEmpty()) return false;
        front = (front + 1) % size;
        count--;
        return true;
    }
    
    public int Front() {
        if (isEmpty()) return -1;
        return data[front];
    }
    
    public int Rear() {
        if (isEmpty()) return -1;
        return data[rear];
    }
    
    public boolean isEmpty() {
        return count == 0;
    }
    
    public boolean isFull() {
        return count == size;
    }
}


/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue obj = new MyCircularQueue(k);
 * boolean param_1 = obj.enQueue(value);
 * boolean param_2 = obj.deQueue();
 * int param_3 = obj.Front();
 * int param_4 = obj.Rear();
 * boolean param_5 = obj.isEmpty();
 * boolean param_6 = obj.isFull();
 */