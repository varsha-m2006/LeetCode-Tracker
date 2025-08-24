#PROBLEM 224 - STACKS
#BASIC CALCULATOR 3

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        num = 0
        last_op = '+'
        s = s.replace(" ", "")

        for i, char in enumerate(s):
            if char.isdigit():
                num = num * 10 + int(char)

            if char == '(':
                stack.append(last_op)
                stack.append('(')
                last_op = '+'
                num = 0

            if char in '+-*/)' or i == len(s) - 1:
                
                if last_op == '+':
                    stack.append(num)
                elif last_op == '-':
                    stack.append(-num)
                elif last_op == '*':
                    stack.append(stack.pop() * num)
                elif last_op == '/':
                    top = stack.pop()
                    if top < 0:
                        stack.append(-(-top // num))
                    else:
                        stack.append(top // num)

                num = 0  

                
                if char == ')':
                    subtotal = 0
                    while stack[-1] != '(':
                        subtotal += stack.pop()
                    stack.pop()  

                    
                    op = stack.pop()
                    if op == '+':
                        stack.append(subtotal)
                    elif op == '-':
                        stack.append(-subtotal)
                    elif op == '*':
                        stack.append(stack.pop() * subtotal)
                    elif op == '/':
                        top = stack.pop()
                        if top < 0:
                            stack.append(-(-top // subtotal))
                        else:
                            stack.append(top // subtotal)
                else:
                    last_op = char

        return sum(stack)
