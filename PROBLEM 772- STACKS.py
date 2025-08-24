#PROBLEM 224 - STACKS
#BASIC CALCULATOR 3

class Solution(object):
    def calculate(self, s):
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

                # Apply last operator to current number
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

                # Process closing parenthesis
                if char == ')':
                    # Build a local stack for this parentheses
                    temp_stack = []
                    while stack[-1] != '(':
                        temp_stack.append(stack.pop())
                    temp_stack.reverse()  # restore original order
                    stack.pop()  # remove '('

                    # Operator before '('
                    op = stack.pop()

                    # Evaluate the local stack with proper *,/ precedence
                    local_num = temp_stack[0]
                    local_op = '+'
                    for j in range(1, len(temp_stack), 2):
                        operator = temp_stack[j]
                        next_num = temp_stack[j+1]
                        if operator == '+':
                            local_num += next_num
                        elif operator == '-':
                            local_num -= next_num
                        elif operator == '*':
                            local_num *= next_num
                        elif operator == '/':
                            if local_num < 0:
                                local_num = -(-local_num // next_num)
                            else:
                                local_num = local_num // next_num

                    # Apply operator before '('
                    if op == '+':
                        stack.append(local_num)
                    elif op == '-':
                        stack.append(-local_num)
                    elif op == '*':
                        stack.append(stack.pop() * local_num)
                    elif op == '/':
                        top = stack.pop()
                        if top < 0:
                            stack.append(-(-top // local_num))
                        else:
                            stack.append(top // local_num)

                else:
                    last_op = char

        return sum(stack)
