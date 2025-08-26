#PROBLEM 153 - BINARY SEARCH
#FIND MINIMUM IN ROTATED SORTED ARRAY

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left=0
        right=len(nums)-1
        
        #binary search
        while left<right:
            m=(left+right)//2

            #finding infliction
            if nums[m]>nums[right]:
                left=m+1
            else:
                right=m

        #returning the minimum element
        return nums[left]

        
        