#PROBLEM 150 - STACK
#EVALUATE REVERSE POLISH NOTATION

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        #stack
        l=[]

        #looping through all elements
        for i in tokens:

            #if operand is +
            if i=='+':
                #pop out last two elements and push its sum into stack
                r=l.pop()
                h=l.pop()
                l.append(int(h)+int(r))
            #similarly for rest of the operands
            elif i=='*':
                r=l.pop()
                h=l.pop()
                l.append(int(h)*int(r))
            elif i=='-':
                r=l.pop()
                h=l.pop()
                l.append(int(h)-int(r))
            elif i=='/':
                r=l.pop()
                h=l.pop()
                l.append(int(float(h) / r))
            #if a number instead if an operand push into stack
            else:
                l.append(int(i))
        #first element in the stackk now with only one number is the value of the expression
        for i in l:
            return i

        