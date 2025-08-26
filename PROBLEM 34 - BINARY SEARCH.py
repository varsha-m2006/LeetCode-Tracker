#PROBLEM 34 - BINARY SEARCH
#FIND FIRST AND LAST POSITION OF ELEMENT IN SORTED ARRAY

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        #find the first and last occurances
        def findBound(isFirst):
            left=0
            right=len(nums)-1

            bound=-1

            #binary search
            while left<=right:
                m=(left+right)//2

                #if found 
                if nums[m]==target:
                    bound =m 

                    #if you want to find the first occurance u go back
                    if isFirst:
                        right=m-1
                    
                    #or u go forwards
                    else:
                        left=m+1
                elif nums[m]<target:
                    left=m+1
                else:
                    right=m-1
            return bound

        #first and last occurance
        return [findBound(True),findBound(False)]