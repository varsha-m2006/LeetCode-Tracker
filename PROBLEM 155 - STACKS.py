#PROBLEM 155 - STACKS
#MIN STACK

class MinStack(object):
    #constructor for stack
    def __init__(self):
        self.stack=[]

    #pushing in elements
    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)

    #elements at the top get popped, LIFO
    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        
    #peak elememt
    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        
    #minimum number in stack
    def getMin(self):
        """
        :rtype: int
        """
        return min(self.stack)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()