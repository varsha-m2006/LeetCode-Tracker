#PROBLEM 20 - STACKS
#VALID PARENTHESES

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #initializing stack
        stack=[]

        #mapping closing and opening brackets
        mapping={')':'(','}':'{',']':'['}

        #loping through all characters in string
        for char in s:
            #if char is a closing bracket
            if char in mapping:
                top=stack.pop() if stack else "#"
                
                #if top of the list is not the opening bracket corresponding to char
                if mapping[char]!=top:
                    return False
            #opening brackets pushed in stack
            else:
                stack.append(char)

        
        #stack is empty by the end, returns TRUE if bracets close in correct order
        return not stack

        


        