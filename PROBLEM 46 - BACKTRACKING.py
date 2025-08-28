#PROBLEM 46 - BACKTRACKING
#PERMUTATIONS

class Solution(object):
    
    #here you dont care much about the order you only care if the elements are used
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []

        def backtrack(path, used):
            # Base case: when path has all nums
            if len(path) == len(nums):
                res.append(path[:])   # make a copy
                return

            # Try every number
            for i in range(len(nums)):
                if used[i]:   # skip if this num already used
                    continue
                # choose
                used[i] = True
                path.append(nums[i])
                # recurse
                backtrack(path, used)
                # undo
                path.pop()
                used[i] = False

        backtrack([], [False]*len(nums))
        return res
