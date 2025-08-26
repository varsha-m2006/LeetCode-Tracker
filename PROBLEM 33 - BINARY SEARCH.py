#PROBLEM 33 - BINARY SEARCH
#SEARCH IN ROTATED SORTED ARRAY

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1

        #binary search
        while left <= right:
            m = (left + right) // 2

            if nums[m] == target:
                return m

            #left half is sorted
            if nums[m] >= nums[right]:
                #if its between the left and middle element 
                if nums[left] <= target < nums[m]:
                    right = m - 1
                else:
                    left = m + 1
            #right half is sorted
            else:
                #if its between the middle element and the right
                if nums[m] < target <= nums[right]:
                    left = m + 1
                else:
                    right = m - 1

        return -1

        