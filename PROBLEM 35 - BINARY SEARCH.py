#PROBLEM 35 - BINARY SEARCH
#SEARCH INSERT POSITION

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left=0
        right=len(nums)-1
        
        #binary search
        while left<=right:
            m=(left+right)//2
            if nums[m]==target:
                return m
            elif nums[m]<target:
                left=m+1
            else:
                right=m-1

        #the position it could be in 
        return left
                

        


        
        