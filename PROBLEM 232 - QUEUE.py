#PROBLEM 232 - QUEUE
#IMPLEMENT QUEUE USING STACKS

class MyQueue(object):

    #constructor
    def __init__(self):
        self.stack=[]
        
    #add to end of list
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        return self.stack.append(x)
        
    #popped from begging, FIF0
    def pop(self):
        """
        :rtype: int
        """
        return self.stack.pop(0)
        
    #top-most element
    def peek(self):
        """
        :rtype: int
        """
        return self.stack[0]
        
    #if length = 0
    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()