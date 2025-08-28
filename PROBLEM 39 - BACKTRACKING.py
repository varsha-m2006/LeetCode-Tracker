#PROBLEM 39 - BACKTRACKING
#COMBINATION SUM

class Solution(object):

    #here order is imporant not what is used more than once when it comes to combinations
    def combinationSum(self, nums, target):
        res = []

        def backtrack(start, path, total):
            if total == target:
                res.append(path[:])
                return
            if total > target:
                return

            for i in range(start, len(nums)):
                # choose nums[i]
                path.append(nums[i])
                # since we can reuse nums[i], call backtrack with i (not i+1)
                backtrack(i, path, total + nums[i])
                # undo choice
                path.pop()

        backtrack(0, [], 0)
        return res
