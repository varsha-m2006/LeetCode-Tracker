#PROBLEM 162 - BINARY SEARCH
#FIND PEAK ELEMENT

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left=0
        right=len(nums)-1
        
        #binary search
        while left<right:
            m=(left+right)//2

            #if there is an element greater move to right portion
            if nums[m]<nums[m+1]:
                left=m+1
            #or else move to left
            else:
                right=m

        #returning peak element
        return left


        