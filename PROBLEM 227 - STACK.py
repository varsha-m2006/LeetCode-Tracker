#PROBLEM 227 - STACK
#BASIC CALCULATOR II

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        #stack initialization
        stack=[]

        #for saving previous number
        num=0

        #initialized for now as +
        last_op='+'

        for i,char in enumerate(s):

            #if char is a number, incase its two digit
            if char.isdigit():
                num=num*10+int(char)

            #if an operand
            if char in '+-*/' or i==len(s)-1:

                #if + or - pushing into stack as those operation are dealt with last
                if last_op == '+':
                    stack.append(num)
                elif last_op == '-':
                    stack.append(-num)

                #if * or - pop out the top element and the orev elemnt operation pushed into stack
                elif last_op == '*':
                    stack.append(stack.pop() * num)
                elif last_op == '/':
                    #truncate toward zero
                    top = stack.pop()
                    if top < 0:
                        stack.append(-(-top // num))
                    else:
                        stack.append(top // num)

                #re setting
                last_op = char
                num = 0

        #addition done at last
        return sum(stack)



        
        
        