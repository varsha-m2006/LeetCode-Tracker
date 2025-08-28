#PROBLEM 17 - BACKTRACKING
#LETTER COMBINATIONS OF A PHONE NUMBER

class Solution(object):
    def letterCombinations(self, digits):
        if not digits:   # if input is empty, no combos
            return []

        digit_to_letters = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        res = []

        def backtrack(index, path):
            # base case: when we've chosen letters for all digits
            if index == len(digits):
                res.append("".join(path))  # join path like ['a','d'] -> "ad"
                return

            # step 1: take the current digit
            current_digit = digits[index]
            # step 2: get all letters that digit can map to
            for ch in digit_to_letters[current_digit]:
                # step 3: choose one letter
                path.append(ch)
                # step 4: recurse to the NEXT digit
                backtrack(index + 1, path)
                # step 5: undo (backtrack)
                path.pop()

        backtrack(0, [])
        return res
