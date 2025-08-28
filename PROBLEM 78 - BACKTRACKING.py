#PROBLEM 78 - BACKTRACKING
#SUBSETS

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        #result
        res=[]

        #to store new solutions and remove the previous ones
        def backtrack(start,path):

            #each of the subsets stored
            res.append(path[:])

            #adding each of the subsets and popping
            for i in range(start,len(nums)):
                path.append(nums[i])

                #recursive call
                backtrack(i+1,path)
                path.pop()
        
        #callback
        backtrack(0,[])

        #returning all subsets
        return res
        