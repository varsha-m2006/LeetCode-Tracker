#PROBLEM 22 - BACKTRACKING
#GENERATE PARENTHESES

class Solution(object):
    def generateParenthesis(self, n):
        res = []

        def backtrack(path, open_count, close_count):

            #base case
            if len(path) == 2 * n:
                res.append("".join(path))
                return
            
            #adding the opening brackets
            if open_count < n:
                path.append('(')

                #recursive call
                backtrack(path, open_count + 1, close_count)
                path.pop()
            
            #adding the closing brackets
            if close_count < open_count:
                path.append(')')

                #recursive call
                backtrack(path, open_count, close_count + 1)
                path.pop()

        backtrack([], 0, 0)
        return res
