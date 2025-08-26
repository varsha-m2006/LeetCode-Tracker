#PROBLEM 704 - BINARY SEARCH
#BINARY SEARCH

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #left pointer
        left=0

        #right pointer
        right=len(nums)-1

        #binary search
        while left<=right:

            #middle element
            m=(left+right)//2

            #if found index returned
            if nums[m]==target:
                return m

            #if lesser than target, moves to right partition
            elif nums[m]<target:
                left=m+1

            #left partition
            else:
                right=m-1
                
        #if not found
        return -1
        