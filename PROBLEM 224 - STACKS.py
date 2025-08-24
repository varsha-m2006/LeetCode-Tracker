#PROBLEM 224 - STACKS
#BASIC CALCULATOR

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        #for the numbers
        stack = []
        #previous number
        num = 0
        last_op = '+'  #assume a + before first number
        s = s.replace(" ", "")  #remove spaces for simplicity

        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)  #build multi-digit number

            #if parenthesis open
            if char == '(':
                #push the previous operator inside
                stack.append(last_op)
                #then the opening bracket
                stack.append('(')

                #re set to default which is +
                last_op = '+'  
                #re set
                num = 0

            #operator or )
            if char in '+-)' or i == len(s) - 1:
                if char == ')':
                    #operation if + or - push num into stack with appropriate sign
                    if last_op == '+':
                        stack.append(num)
                    elif last_op == '-':
                        stack.append(-num)
                        
                    #resetting
                    num = 0

                    sums = 0
                    #pop out all till u see opening bracket
                    while stack[-1] != '(':
                        sums += stack.pop()
                    stack.pop()  #remove '('

                    #apply operator before '('
                    op = stack.pop()
                    #then based on the operator push the sum in with appropriate signs
                    if op == '-':
                        sums = -sums
                    stack.append(sums)
                    last_op = '+'  #reset
                else:
                    #handle regular + or -
                    if last_op == '+':
                        stack.append(num)
                    elif last_op == '-':
                        stack.append(-num)

                    #resetting
                    num = 0
                    last_op = char

        return sum(stack)
